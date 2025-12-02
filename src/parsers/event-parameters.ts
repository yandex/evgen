import { populateCustomTypesDeep } from '../helpers';
import { ParameterType, PrimitiveType } from '../types/data-types';
import { EventParameter } from '../types/parsed-types';
import { RawEventParameter } from '../types/raw-types';
import { validateParameter } from '../validators/parameter-validator';

interface ParseParametersOptions {
    scope: string;
    namespace?: string;
    version?: number;
}

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
        });
        parsedParams.push({
            name,
            namespace,
            version,
            type: populateCustomTypesDeep(parameter.type, name) as ParameterType,
            description: parameter.description || '',
            defaultValue: parameter.default_value,
            abstract: parameter.abstract || false,
            optional: parameter.optional || false,
            elementType: populateCustomTypesDeep(parameter.element_type, name) as PrimitiveType,
        });
    });

    return parsedParams;
};
