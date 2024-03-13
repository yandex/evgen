import { flatten, sortBy } from 'lodash';

import { InterfaceVersion, NamespaceCollection } from '../types/parsed-types';
import { RawEvents } from '../types/raw-types';

import {
    EVENTS_FIELD,
    GLOBAL_PARAMETERS_FIELD,
    SHARED_FIELD,
    INTERFACES_FIELD,
    PLATFORM_PARAMETERS_FIELD,
} from './constants';
import { parseEventNamespaces } from './events';
import { parseGlobalParameters } from './global-event-parameters';
import { getLatestCompatibleVersion } from './interface-compatibility';
import { parseInterfaces } from './interfaces';
import { parsePlatformParameters } from './platform-parameters';

export const parseEvents = (rawEvents: RawEvents): NamespaceCollection => {
    const globalParameters =
        rawEvents[GLOBAL_PARAMETERS_FIELD] &&
        parseGlobalParameters(rawEvents[GLOBAL_PARAMETERS_FIELD]);
    const platformParameters =
        (rawEvents[PLATFORM_PARAMETERS_FIELD] &&
            parsePlatformParameters(rawEvents[PLATFORM_PARAMETERS_FIELD])) ||
        {};
    const eventNamespaces = parseEventNamespaces(rawEvents[EVENTS_FIELD]);
    const interfaceDict =
        rawEvents[INTERFACES_FIELD] && parseInterfaces(rawEvents[INTERFACES_FIELD]);

    const interfaceNamespaces: Record<string, InterfaceVersion[]> = {};

    if (interfaceDict) {
        sortBy(Object.entries(interfaceDict), (item) => item[0]) // sort by namespace for order in docs
            .forEach(([interfaceNamespace, events]) => {
                interfaceNamespaces[interfaceNamespace] = flatten(Object.values(events));
            });

        eventNamespaces.forEach((namespace) =>
            namespace.events.forEach((event) =>
                event.versions.forEach((eventVersion) => {
                    if (eventVersion.interfaceNames?.length) {
                        const interfaces: Record<string, number> = {};
                        eventVersion.interfaceNames.forEach((interfaceFullName) => {
                            const interfaceParts = interfaceFullName.split('.', 2);
                            const [namespace, name] =
                                interfaceParts.length > 1
                                    ? interfaceParts
                                    : [INTERFACES_FIELD, interfaceParts[0]];
                            if (!interfaceDict[namespace] || !interfaceDict[namespace][name]) {
                                console.log(`Interface ${interfaceFullName} not found.`);
                                return;
                            }
                            const latestVersion = getLatestCompatibleVersion(
                                eventVersion,
                                interfaceDict[namespace][name],
                                globalParameters.parameters
                            );
                            if (latestVersion) {
                                interfaces[interfaceFullName] = latestVersion;
                            } else {
                                console.log(
                                    `Event ${eventVersion.namespace}:${eventVersion.name} is not compatible with ${interfaceFullName}`
                                );
                            }
                        });

                        eventVersion.interfaces = interfaces;
                    }
                })
            )
        );
    }
    return {
        globalParameters,
        platformParameters,
        eventNamespaces,
        interfaceNamespaces,
        shared: rawEvents[SHARED_FIELD],
    };
};
