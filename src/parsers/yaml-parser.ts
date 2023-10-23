import { readFile, lstat } from 'fs/promises';
import { join } from 'path';

import { parse as yamlParse } from 'yaml';
import fg from 'fast-glob';
import { isObject, get, merge } from 'lodash';

const INCLUDE_TAG = '!include';
const INCLUDED_PREFIX = '_included';
const MERGED_PREFIX = '_merged';
const YAML_FILE_PATTERN = '**/*.yaml';

let mergedCount = 1;

const parseYamlFile = async (file: string) => {
    const yamlData = await readFile(file, { encoding: 'utf-8' });
    const replaceMergeKeys = yamlData.replaceAll(
        '<<:',
        // eslint-disable-next-line no-plusplus
        () => `${MERGED_PREFIX}_${mergedCount++}:` // use counter to make merge key unique
    );
    return yamlParse(replaceMergeKeys.replace(/\*(\S+):(\s)/g, '*$1 :$2'), {
        uniqueKeys: false,
        maxAliasCount: -1,
        customTags: [
            {
                tag: INCLUDE_TAG,
                resolve: (str: string) => `${INCLUDE_TAG}:${str}`,
            },
        ],
    });
};

type NodeType = Record<string, unknown> | string | boolean | number;

const replaceMerges = (node: unknown): unknown => {
    const merged: Record<string, unknown> = {};
    const own: Record<string, unknown> = {};

    if (isObject(node)) {
        const allKeys = Object.keys(node);
        const mergeKeys = allKeys.filter((key) => key.startsWith(MERGED_PREFIX));
        mergeKeys.forEach((key) => {
            const value = (node as Record<string, unknown>)[key];
            if (!isObject(value)) {
                throw new Error(`Included value should be object, but got ${value}`);
            }
            Object.assign(merged, replaceMerges(value));

            delete (node as Record<string, unknown>)[key];
        });

        const ownKeys = allKeys.filter((key) => !key.startsWith(MERGED_PREFIX));
        ownKeys.forEach((key) => {
            const value = (node as Record<string, unknown>)[key];
            own[key] = replaceMerges(value);

            delete (node as Record<string, unknown>)[key];
        });

        // Order according to original evgen for compatibility
        Object.assign(node, merged, own);
    }

    return node;
};

const replaceIncludes = (node: NodeType, eventsByFile: Record<string, unknown>): unknown => {
    if (typeof node === 'string' && node.startsWith(INCLUDE_TAG)) {
        const [, file, path] = node.split(':');
        const includedNode = get(eventsByFile[file], path);
        if (!includedNode) {
            throw new Error(`Failed to include ${file}: ${path}. Initial value is ${node}`);
        }

        return replaceIncludes(includedNode, eventsByFile);
    }

    if (isObject(node)) {
        const included: Record<string, unknown> = {};
        const own: Record<string, unknown> = {};

        Object.entries(node).forEach(([key, value]) => {
            const newValue = replaceIncludes(value as NodeType, eventsByFile);
            if (key.startsWith(INCLUDED_PREFIX)) {
                if (!isObject(newValue)) {
                    throw new Error(`Included value should be object, but got ${newValue}`);
                }
                Object.assign(included, newValue);
            } else {
                own[key] = newValue;
            }
            delete node[key];
        });

        // Order according to original evgen for compatibility
        return Object.assign(node, included, own);
    }

    return node;
};

export const parseConfigFile = async (filePath: string) => parseYamlFile(filePath);

export const parseEventsFile = async (eventsPath: string) => {
    const eventSource = await lstat(eventsPath);
    if (eventSource.isFile()) {
        const fileData = await parseYamlFile(eventsPath);
        return replaceMerges(fileData);
    }

    if (eventSource.isDirectory()) {
        const yamlFiles = await fg(YAML_FILE_PATTERN, { cwd: eventsPath });
        const events: Record<string, unknown> = {};
        const eventsByFile: Record<string, unknown> = {};
        await Promise.all(
            yamlFiles.map(async (fileName: string) => {
                const fileData = await parseYamlFile(join(eventsPath, fileName));
                const fileDataProcessed = replaceMerges(fileData);
                eventsByFile[fileName.replace(/\.yaml$/, '')] = fileDataProcessed;
                merge(events, fileDataProcessed);
            })
        );

        return replaceIncludes(events, eventsByFile);
    }

    throw new Error(`Invalid events path: ${eventsPath}`);
};
