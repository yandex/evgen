import { populateCustomTypesDeep } from '../helpers';
import { ParameterType, PrimitiveType } from '../types/data-types';
import { EventParameter } from '../types/parsed-types';
import { RawEventParameter, RawPlatform } from '../types/raw-types';
import { validateParameter } from '../validators/parameter-validator';

interface ParseParametersOptions {
    scope: string;
    namespace?: string;
    version?: number;
}

export const parseParametersFromEventPlatforms = (
    platforms: Record<string, RawPlatform> | undefined,
    { scope, namespace = '', version = 1 }: ParseParametersOptions
): Record<string, EventParameter<ParameterType>[]> | undefined => {
    if (!platforms) {
        return undefined;
    }
    const result: Record<string, EventParameter<ParameterType>[]> = {};
    Object.entries(platforms).forEach(([platformKey, raw]) => {
        const parsed = parseParameters(raw.parameters ?? null, {
            namespace,
            version,
            scope: `${scope}.platforms.${platformKey}.parameters`,
        });
        if (parsed.length) {
            result[platformKey] = parsed;
        }
    });
    return Object.keys(result).length ? result : undefined;
};

export const parseParameters = (
    parameters: Record<string, RawEventParameter> | null,
    { scope, namespace = '', version = 1 }: ParseParametersOptions
): EventParameter<ParameterType>[] => {
    const parsedParams: EventParameter<ParameterType>[] = [];
    if (!parameters) {
        return parsedParams;
    }
    Object.entries(parameters).forEach(([name, parameter], index) => {
        validateParameter(parameter, {
            key: name,
            path: `${scope}.v${version}.[${index}]`,
            allParameters: parameters,
        });
        parsedParams.push({
            name,
            namespace,
            version,
            type: populateCustomTypesDeep(parameter.type, name) as ParameterType,
            description: parameter.description || '',
            defaultValue:
                parameter.default_value !== undefined
                    ? parameter.default_value
                    : parameter.optional
                    ? null
                    : undefined,
            abstract: parameter.abstract || false,
            optional: parameter.optional || false,
            elementType: populateCustomTypesDeep(parameter.element_type, name) as PrimitiveType,
        });
    });

    return parsedParams;
};
