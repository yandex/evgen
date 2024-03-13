import { isPlatformConst } from '../helpers/const';
import {
    ConstType,
    ParameterType,
    PlatformConstType,
    SinglePlatformParameterType,
} from '../types/data-types';
import { EventParameter, EventVersion, NamespaceCollection } from '../types/parsed-types';
import {
    SinglePlatformEventVersion,
    SinglePlatformNamespaceCollection,
} from '../types/single-platform-types';

export const singlePlatformEvents = (
    events: NamespaceCollection,
    platform: string,
    { onlyLastVersion = false }
): SinglePlatformNamespaceCollection => {
    const platformParameters =
        events.platformParameters && events.platformParameters[platform]
            ? events.platformParameters[platform]
            : { parameters: [] };
    return {
        globalParameters: events.globalParameters
            ? {
                  ...events.globalParameters,
                  parameters: parseSinglePlatformParameters(
                      events.globalParameters.parameters,
                      platform
                  ),
              }
            : { description: '', parameters: [] },
        platformParameters: {
            ...platformParameters,
            parameters: parseSinglePlatformParameters(platformParameters.parameters, platform),
        },
        eventNamespaces: events.eventNamespaces
            .map((namespace) => {
                const events = namespace.events
                    .map((event) => ({
                        ...event,
                        versions: parsePlatformEventVersions(event.versions, platform, {
                            onlyLastVersion,
                        }),
                    }))
                    .filter((event) => event.versions.length);

                return {
                    ...namespace,
                    events,
                };
            })
            .filter((namespace) => namespace.events.length),
        shared: events.shared,
    };
};

const parseSinglePlatformParameters = (
    parameters: EventParameter<ParameterType>[],
    platform: string
): EventParameter<SinglePlatformParameterType>[] =>
    parameters.map(
        (parameter) =>
            ({
                ...parameter,
                type: isPlatformConst(parameter.type)
                    ? parsePlatformConstType(parameter.type, platform)
                    : parameter.type,
            }) as EventParameter<SinglePlatformParameterType>
    );

const parsePlatformConstType = (
    platformConstType: PlatformConstType,
    platform: string
): ConstType | undefined => {
    const platformConstValue = platformConstType.PlatformConst[platform];
    if (platformConstValue === undefined) {
        return undefined;
    }
    return { Const: platformConstValue };
};

const parsePlatformEventVersions = (
    eventVersions: EventVersion[],
    platformName: string,
    { onlyLastVersion = false }
): SinglePlatformEventVersion[] => {
    const allPlatformVersions = eventVersions
        .filter((eventVersion) => {
            if (!eventVersion.platforms) {
                return false;
            }

            const platform = eventVersion.platforms[platformName];
            if (!platform || platform.lastVersion !== null) {
                return false;
            }

            return true;
        })
        .map((version) => ({
            ...version,
            platform: platformName,
            parameters: parseSinglePlatformParameters(version.parameters, platformName),
        }));

    if (allPlatformVersions.length === 0) {
        return [];
    }

    if (onlyLastVersion) {
        const lastVersion = allPlatformVersions[allPlatformVersions.length - 1];
        lastVersion.parameters.forEach((p) => {
            // Not specify version in names if onlyLastVersion (see typeFormat handlebars helper)
            // TODO: move this logic to hbs template
            p.version = 1;
        });
        return [lastVersion];
    }

    return allPlatformVersions;
};
