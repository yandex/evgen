import { get, isObject } from 'lodash';

import { EventNamespace, EventVersion, Event } from '../types/parsed-types';
import { NestedRecord, RawEvent } from '../types/raw-types';

import { parseParameters } from './event-parameters';
import { parsePlatforms } from './platforms';
import { VERSION_PATTERN } from './constants';
import { upperFirstLetter } from '../helpers';

const DEFAULT_NAMESPACE_NAME = 'Singletons';

export const parseEventNamespaces = (
    rawEventsNamespaces: Record<string, NestedRecord<NestedRecord<RawEvent>>>
): EventNamespace<Event>[] => {
    const docDirs: Record<string, string> = {};

    const eventVersions = Object.entries(rawEventsNamespaces).flatMap(([eventKey, eventNode]) => {
        if (get(eventNode, 'documentation_dir')) {
            docDirs[eventKey] = String(get(eventNode, 'documentation_dir'));
        }
        return parseEventVersions([eventKey], eventNode);
    });
    const eventsByNamespace = getEventsByNamespace(eventVersions);

    return Object.entries(eventsByNamespace)
        .map(([namespace, namespaceEvents]) => ({
            name: namespace,
            events: Object.entries(getEventsByName(namespaceEvents)).map(([name, versions]) => {
                if (versions.length > 1) {
                    versions.sort((v1, v2) => v1.version - v2.version);
                }
                return {
                    name,
                    versions,
                };
            }),
            documentationDir: docDirs[namespace],
        }))
        .sort((n1, n2) => {
            if (n1.name < n2.name) {
                return -1;
            }
            if (n1.name > n2.name) {
                return 1;
            }
            return 0;
        });
};

const getEventsByNamespace = (eventVersions: EventVersion[]): Record<string, EventVersion[]> =>
    eventVersions.reduce<Record<string, EventVersion[]>>((eventsByNamespace, event) => {
        const { namespace } = event;
        if (!eventsByNamespace[namespace]) {
            eventsByNamespace[namespace] = [event];
        } else {
            eventsByNamespace[namespace].push(event);
        }
        return eventsByNamespace;
    }, {});

const getEventsByName = (eventVersions: EventVersion[]): Record<string, EventVersion[]> =>
    eventVersions.reduce<Record<string, EventVersion[]>>((eventsByName, event) => {
        const { name } = event;
        if (!eventsByName[name]) {
            eventsByName[name] = [event];
        } else {
            eventsByName[name].push(event);
        }
        return eventsByName;
    }, {});

const parseEventVersions = (
    namespaceParts: string[],
    node: NestedRecord<NestedRecord<RawEvent>>
): EventVersion[] => {
    const namespace = namespaceParts.length > 0 ? namespaceParts[0] : DEFAULT_NAMESPACE_NAME;
    return Object.entries(node).flatMap(([key, value]: [string, NestedRecord<RawEvent>]) => {
        const versionKeyMatch = key.match(VERSION_PATTERN);
        if (versionKeyMatch && versionKeyMatch[1] && isEventNode(value)) {
            const name = namespaceParts.map(upperFirstLetter).join('');

            const version = parseInt(versionKeyMatch[1], 10);

            if (value.namespaces) {
                value.namespaces.forEach((namespace) => {
                    if (typeof namespace !== 'string') {
                        throw new Error(
                            `Failed to parse namespace ${JSON.stringify(
                                namespace
                            )}: namespace must be string!`
                        );
                    }
                });
            }

            return [
                {
                    name,
                    namespace,
                    event: value.force_event_name || namespaceParts.join('.'),
                    version,
                    parameters: parseParameters(value.parameters, name, version),
                    description: value.description || '',
                    comment: value.comment,
                    platforms: value.platforms ? parsePlatforms(value.platforms) : undefined,
                    interfaceNames: getInterfaceNames(value.interface),
                    interfaces: {},
                    additionalNamespaces: value.namespaces || [],
                },
            ];
        }

        if (key === 'documentation_dir' || key === 'inheritance') {
            return [];
        }

        return isObject(value)
            ? parseEventVersions(
                  [...namespaceParts, key],
                  value as NestedRecord<NestedRecord<RawEvent>>
              )
            : [];
    });
};

const getInterfaceNames = (value: unknown): string[] => {
    if (!value) {
        return [];
    }

    return Array.isArray(value) ? value : [value];
};

const isEventNode = (node: NestedRecord<NestedRecord<RawEvent>>): node is RawEvent =>
    node.parameters !== undefined && node.description !== undefined;
