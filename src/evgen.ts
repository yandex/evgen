import { rm } from 'fs/promises';
import { resolve } from 'path';

import { groupBy, sortBy, uniq, uniqBy } from 'lodash';

import { compileTemplates } from './compiler';
import { CodeLanguage } from './types/evgen-config';
import { EventNamespace, Event, NamespaceCollection, EventVersion } from './types/parsed-types';
import { SinglePlatformNamespaceCollection } from './types/single-platform-types';

const DEFAULT_CLASS_NAME = 'EvgenAnalytics';

interface GenerateOptions {
    outputPath: string;
    templateDir: string;
}

interface CodeGenerateOptions extends GenerateOptions {
    className?: string;
    onlyLastVersion?: boolean;
}

export const generateEventsCode = async (
    language: CodeLanguage,
    events: SinglePlatformNamespaceCollection,
    options: CodeGenerateOptions
) => {
    await prepareOutDir(resolve(options.outputPath));

    const eventNamespaces = events.eventNamespaces.map(extendNamespaceData);
    const namedEnums = uniqBy(
        eventNamespaces.flatMap((namespace) => namespace.namedEnums),
        'type.Enum.name'
    );

    const allVersionsByEvent = groupAllVersionsByEvent(events.eventNamespaces);

    const ctx = {
        ...events,
        eventNamespaces,
        allVersionsByEvent,
        namedEnums,
        onlyLastVersion: options.onlyLastVersion,
        classname: options.className || DEFAULT_CLASS_NAME,
    };

    return compileTemplates(ctx, {
        language,
        templateDir: options.templateDir,
        outputPath: options.outputPath,
    });
};

export const generateEventsDocs = async (events: NamespaceCollection, options: GenerateOptions) => {
    const { templateDir, outputPath } = options;
    await prepareOutDir(resolve(outputPath));

    const eventNamespacesByDocDir = groupBy(
        sortBy(events.eventNamespaces.map(extendNamespaceData), 'documentationDir'),
        'documentationDir'
    );

    const allVersionsByEvent = groupAllVersionsByEvent(events.eventNamespaces);

    const ctx = {
        ...events,
        allVersionsByEvent,
        eventNamespacesByDocDir,
    };

    return compileTemplates(ctx, {
        templateDir,
        outputPath,
    });
};

const groupAllVersionsByEvent = (eventNamespaces: EventNamespace<Event>[]) => {
    const allVersionsByEvent: Record<string, EventVersion[]> = {};
    sortBy(eventNamespaces, 'name').forEach((namespace) => {
        namespace.events.forEach((namespaceEvents) => {
            namespaceEvents.versions.forEach((version) => {
                const eventNames = version.additionalNamespaces.length
                    ? version.additionalNamespaces.map(
                          (namespace) => `${namespace}.${version.event}`
                      )
                    : [version.event];
                eventNames.forEach((eventName) => {
                    allVersionsByEvent[eventName] = allVersionsByEvent[eventName]
                        ? [...allVersionsByEvent[eventName], version]
                        : [version];
                });
            });
        });
    });

    return allVersionsByEvent;
};

const prepareOutDir = async (outDir: string) => rm(outDir, { recursive: true, force: true });

const extendNamespaceData = (namespace: EventNamespace<Event>) => {
    const allVersions = namespace.events.flatMap((e) => e.versions);
    const actualVersions = allVersions.filter(
        (eventVersion) =>
            eventVersion.platforms &&
            Object.values(eventVersion.platforms).some((platform) => platform.lastVersion === null)
    );
    const deprecatedVersions = allVersions.filter(
        (eventVersion) =>
            eventVersion.platforms &&
            Object.values(eventVersion.platforms).every((platform) => platform.lastVersion !== null)
    );
    const namedEnums = uniqBy(
        namespace.events.flatMap((e) => e.versions.flatMap((v) => v.parameters)),
        'type.Enum.name'
    );
    const allPlatforms = uniq(
        namespace.events.flatMap((e) =>
            e.versions.flatMap((version) => Object.keys(version.platforms || {}))
        )
    );

    return {
        ...namespace,
        namedEnums,
        allVersions,
        actualVersions,
        deprecatedVersions,
        allPlatforms,
    };
};
