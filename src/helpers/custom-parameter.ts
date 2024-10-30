import { ParameterType, CustomType } from '../types/data-types';

export const isCustomParameter = (type: ParameterType): type is CustomType =>
    typeof (type as CustomType).Custom === 'object';
