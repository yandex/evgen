import { ParameterType } from '../types/data-types';
import { EventParameter, EventVersion } from '../types/parsed-types';

export const flattenAllEventVersionParameters = (
    version: EventVersion
): EventParameter<ParameterType>[] => [
    ...version.parameters,
    ...(version.parametersPerPlatform ? Object.values(version.parametersPerPlatform).flat() : []),
];
