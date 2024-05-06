import { ParameterType } from '../types/data-types';
import { EventParameter } from '../types/parsed-types';
import { RawEventParameter } from '../types/raw-types';

export const parseParameters = (
    parameters: Record<string, RawEventParameter> | null,
    namespace = '',
    version = 1
): EventParameter<ParameterType>[] => {
    const parsedParams: EventParameter<ParameterType>[] = [];
    if (!parameters) {
        return parsedParams;
    }
    Object.entries(parameters).forEach(([name, parameter]) => {
        parsedParams.push({
            name,
            namespace,
            version,
            type: parameter.type,
            description: (parameter.description || '').replaceAll('\n', ' '),
            defaultValue: parameter.default_value,
            abstract: parameter.abstract || false,
            optional: parameter.optional || false,
            elementType: parameter.element_type,
        });
    });

    return parsedParams;
};
