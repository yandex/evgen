import { readFile, lstat } from 'fs/promises';
import { join } from 'path';

import { parse as yamlParse } from 'yaml';
import fg from 'fast-glob';
import { isObject, get, merge } from 'lodash';
import { assertIsObject } from '../helpers';

const INCLUDE_TAG = '!include';
const INCLUDED_PREFIX = '_included';
const MERGED_PREFIX = '_merged';
const YAML_FILE_PATTERN = '**/*.yaml';

let mergedCount = 1;

type ParseOptions = {
    keepParametersOrder?: boolean;
};

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

const replaceMerges = (node: unknown, parseOptions: ParseOptions): unknown => {
    const primaryFields: Record<string, unknown> = {};
    const secondaryFields: Record<string, unknown> = {};

    if (isObject(node)) {
        const allKeys = Object.keys(node);
        allKeys.forEach((key) => {
            const value = (node as Record<string, unknown>)[key];
            if (key.startsWith(MERGED_PREFIX)) {
                assertIsObject(value);
                Object.assign(primaryFields, replaceMerges(value, parseOptions));
            } else {
                (parseOptions.keepParametersOrder ? primaryFields : secondaryFields)[key] =
                    replaceMerges(value, parseOptions);
            }

            delete (node as Record<string, unknown>)[key];
        });

        Object.assign(node, primaryFields, secondaryFields);
    }

    return node;
};

const replaceIncludes = (
    node: NodeType,
    eventsByFile: Record<string, unknown>,
    parseOptions: ParseOptions
): unknown => {
    if (typeof node === 'string' && node.startsWith(INCLUDE_TAG)) {
        const [, file, path] = node.split(':');
        const includedNode = get(eventsByFile[file], path);
        if (!includedNode) {
            throw new Error(`Failed to include ${file}: ${path}. Initial value is ${node}`);
        }

        return replaceIncludes(includedNode, eventsByFile, parseOptions);
    }

    if (isObject(node)) {
        const primaryFields: Record<string, unknown> = {};
        const secondaryFields: Record<string, unknown> = {};

        Object.entries(node).forEach(([key, value]) => {
            const newValue = replaceIncludes(value as NodeType, eventsByFile, parseOptions);
            if (key.startsWith(INCLUDED_PREFIX)) {
                assertIsObject(newValue);
                Object.assign(primaryFields, newValue);
            } else {
                (parseOptions.keepParametersOrder ? primaryFields : secondaryFields)[key] =
                    newValue;
            }
            delete node[key];
        });

        return Object.assign(node, primaryFields, secondaryFields);
    }

    return node;
};

export const parseConfigFile = async (filePath: string) => parseYamlFile(filePath);

export const parseEventsFile = async (
    eventsPath: string,
    { keepParametersOrder = false }: ParseOptions = {}
) => {
    const eventSource = await lstat(eventsPath);
    if (eventSource.isFile()) {
        const fileData = await parseYamlFile(eventsPath);
        return replaceMerges(fileData, { keepParametersOrder });
    }

    if (eventSource.isDirectory()) {
        const yamlFiles = await fg(YAML_FILE_PATTERN, { cwd: eventsPath });
        const events: Record<string, unknown> = {};
        const eventsByFile: Record<string, unknown> = {};

        // Параллельный парсинг файлов с сохранением алфавитного порядка
        const processedFiles = await Promise.all(
            yamlFiles.sort().map(async (fileName: string) => {
                const fileData = await parseYamlFile(join(eventsPath, fileName));
                const fileDataProcessed = replaceMerges(fileData, { keepParametersOrder });
                return { fileName, fileDataProcessed };
            })
        );

        // Последовательный мерж в объект events с сохранением порядка файлов
        processedFiles.forEach(({ fileName, fileDataProcessed }) => {
            eventsByFile[fileName.replace(/\.yaml$/, '')] = fileDataProcessed;
            merge(events, fileDataProcessed);
        });

        return replaceIncludes(events, eventsByFile, { keepParametersOrder });
    }

    throw new Error(`Invalid events path: ${eventsPath}`);
};
