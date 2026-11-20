import { rm } from 'fs/promises';
import { resolve } from 'path';

import { get, groupBy, sortBy, uniq, uniqBy, uniqWith } from 'lodash';

import { compileTemplates } from './compiler';
import { CodeLanguage, type CaseMode } from './types/evgen-config';
import { SinglePlatformParameterType } from './types/data-types';
import { typeFormat as kotlinTypeFormat } from './languages/kotlin/types';
import {
    EventNamespace,
    Event,
    NamespaceCollection,
    EventVersion,
    EventParameter,
} from './types/parsed-types';
import { SinglePlatformNamespaceCollection } from './types/single-platform-types';
import {
    findNamedEnumsDeepInEvents,
    findNamedCustomTypesDeepInEvents,
    compareCustomTypes,
    flattenAllEventVersionParameters,
    isRef,
    isEnum,
    extractRef,
    pascalCase,
} from './helpers';

const DEFAULT_CLASS_NAME = 'EvgenAnalytics';

interface GenerateOptions {
    outputPath: string;
    templateDir: string;
}

interface CodeGenerateOptions extends GenerateOptions {
    className?: string;
    packageName?: string;
    onlyLastVersion?: boolean;
    disableSendingMeta?: boolean;
    sendMetaEvent?: boolean;
    sendMetaInterfaces?: boolean;
    notSendNullParameters?: boolean;
    paramNameCase?: CaseMode;
    languageVersion?: string;
    splitByNamespace?: boolean;
}

interface DocsGenerateOptions extends GenerateOptions {
    tag?: string;
}

export const generateEventsCode = async (
    language: CodeLanguage,
    events: SinglePlatformNamespaceCollection,
    options: CodeGenerateOptions
) => {
    if (options.packageName && language !== 'kotlin') {
        throw new Error('package_name is only supported for Kotlin');
    }

    if (options.splitByNamespace && language !== 'kotlin') {
        throw new Error('split_by_namespace is only supported for Kotlin');
    }

    const classname = options.className || DEFAULT_CLASS_NAME;
    const eventNamespaces = events.eventNamespaces.map(extendNamespaceData);
    const namedEnums = uniqBy(
        eventNamespaces.flatMap((namespace) => namespace.namedEnums),
        'type.Enum.name'
    );

    const namedCustomParameters = uniqWith(
        eventNamespaces.flatMap((namespace) => namespace.namedCustomParameters),
        compareCustomTypes
    );

    const allVersionsByEvent = groupAllVersionsByEvent(events.eventNamespaces);
    const sharedNamedEnumNames = new Set(
        Object.entries(
            groupBy(
                eventNamespaces.flatMap((namespace) => namespace.namedEnums),
                'type.Enum.name'
            )
        )
            .filter(([, occurrences]) => occurrences.length > 1)
            .map(([name]) => name)
    );
    const sharedNamedEnums = namedEnums.filter((parameter) =>
        sharedNamedEnumNames.has(get(parameter, 'type.Enum.name', ''))
    );
    const outputNamespaces = options.splitByNamespace
        ? eventNamespaces.map((namespace) => ({
              ...namespace,
              namedEnums: namespace.namedEnums.filter(
                  (parameter) => !sharedNamedEnumNames.has(get(parameter, 'type.Enum.name', ''))
              ),
          }))
        : eventNamespaces;

    if (options.splitByNamespace) {
        const classNames = eventNamespaces.map(
            (namespace) => `${classname}${pascalCase(namespace.name)}Events`
        );
        const topLevelNames = [
            ...classNames,
            ...[
                'Tracker',
                'GlobalParamsProvider',
                'PlatformParamsProvider',
                'GlobalParams',
                'PlatformParams',
            ].map((suffix) => `${classname}${suffix}`),
            ...[...events.globalParameters.parameters, ...events.platformParameters.parameters]
                .filter((parameter) => isEnum(parameter.type))
                .map(kotlinTypeFormat),
            ...sharedNamedEnums.map((parameter) =>
                kotlinTypeFormat(parameter as EventParameter<SinglePlatformParameterType>)
            ),
            ...Object.values(events.globalTypes).map((parameter) =>
                isEnum(parameter.type)
                    ? kotlinTypeFormat(parameter as EventParameter<SinglePlatformParameterType>)
                    : pascalCase(parameter.name)
            ),
        ];
        const duplicateName = topLevelNames.find(
            (name, index) => topLevelNames.indexOf(name) !== index
        );
        if (duplicateName) {
            throw new Error(
                `Duplicate Kotlin top-level declaration "${duplicateName}" in split_by_namespace output`
            );
        }
    }

    const ctx = {
        ...events,
        eventNamespaces: outputNamespaces,
        allVersionsByEvent,
        namedEnums,
        sharedNamedEnums,
        namedCustomParameters,
        onlyLastVersion: options.onlyLastVersion,
        classname,
        packageName: options.packageName,
        splitByNamespace: options.splitByNamespace ?? false,
        disableSendingMeta: options.disableSendingMeta,
        sendMetaEvent: options.sendMetaEvent,
        sendMetaInterfaces: options.sendMetaInterfaces,
        notSendNullParameters: options.notSendNullParameters,
        paramNameCase: options.paramNameCase,
        languageVersion: options.languageVersion,
    };

    await prepareOutDir(resolve(options.outputPath));

    return compileTemplates(ctx, {
        language,
        templateDir: options.templateDir,
        outputPath: options.outputPath,
        paramNameCase: options.paramNameCase,
    });
};

export const generateEventsDocs = async (
    events: NamespaceCollection,
    options: DocsGenerateOptions
) => {
    const { templateDir, outputPath, tag } = options;
    await prepareOutDir(resolve(outputPath));

    if (tag) {
        events.eventNamespaces = events.eventNamespaces.map((namespace) => ({
            ...namespace,
            events: namespace.events.map((event) => ({
                ...event,
                versions: event.versions.filter((event) => event.tags?.includes(tag)),
            })),
        }));
    }

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
    const namedEnums = uniqBy(findNamedEnumsDeepInEvents(namespace.events), 'type.Enum.name');
    const namedCustomParameters = uniqWith(
        findNamedCustomTypesDeepInEvents(namespace.events),
        compareCustomTypes
    );
    const allPlatforms = uniq(
        namespace.events.flatMap((e) =>
            e.versions.flatMap((version) => Object.keys(version.platforms || {}))
        )
    );
    const typeRefs = uniq(
        allVersions
            .flatMap((version) => flattenAllEventVersionParameters(version))
            .filter((param) => isRef(param.type))
            .map((param) => pascalCase(extractRef(param.type as string)))
    ).sort();

    return {
        ...namespace,
        namedEnums,
        namedCustomParameters,
        typeRefs,
        allVersions,
        actualVersions,
        deprecatedVersions,
        allPlatforms,
    };
};
