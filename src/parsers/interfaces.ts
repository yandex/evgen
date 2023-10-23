import { groupBy, isObject } from 'lodash';

import { InterfaceVersion } from '../types/parsed-types';
import { NestedRecord, RawInterface } from '../types/raw-types';

import { VERSION_PATTERN, INTERFACES_FIELD } from './constants';
import { parseParameters } from './event-parameters';

export const parseInterfaces = (
    rawInterfaces: Record<string, NestedRecord<NestedRecord<RawInterface>>>
): Record<string, Record<string, InterfaceVersion[]>> => {
    const interfaceVersions = Object.entries(rawInterfaces).flatMap(
        ([interfaceKey, interfaceNode]) => parseInterfaceVersions([interfaceKey], interfaceNode)
    );

    const interfacesByNamespace = groupBy(
        interfaceVersions,
        (interfaceVersion) => interfaceVersion.namespace
    );

    const result: Record<string, Record<string, InterfaceVersion[]>> = {};
    Object.entries(interfacesByNamespace).forEach(([name, interfaceVersions]) => {
        result[name] = groupBy(interfaceVersions, (interfaceVersion) => interfaceVersion.name);
    });

    return result;
};

const parseInterfaceVersions = (
    namespaceParts: string[],
    node: NestedRecord<NestedRecord<RawInterface>>
): InterfaceVersion[] => {
    const namespace = namespaceParts.length > 1 ? namespaceParts[0] : INTERFACES_FIELD;
    const name = namespaceParts.length > 1 ? namespaceParts.slice(1).join('') : namespaceParts[0];
    return Object.entries(node).flatMap(([key, value]) => {
        const versionKeyMatch = key.match(VERSION_PATTERN);
        if (versionKeyMatch && versionKeyMatch[1] && isInterfaceNode(value)) {
            const version = parseInt(versionKeyMatch[1], 10);

            return [
                {
                    name,
                    namespace,
                    version,
                    parameters: parseParameters(value.parameters, name, version),
                    description: value.description || '',
                },
            ];
        }

        return isObject(value)
            ? parseInterfaceVersions(
                  [...namespaceParts, key],
                  value as NestedRecord<NestedRecord<RawInterface>>
              )
            : [];
    });
};

const isInterfaceNode = (node: NestedRecord<NestedRecord<RawInterface>>): node is RawInterface =>
    node.parameters !== undefined;
