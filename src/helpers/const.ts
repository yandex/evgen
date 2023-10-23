import { ParameterType, PlatformConstType, ConstType } from '../types/data-types';

export const isPlatformConst = (parameter: ParameterType): parameter is PlatformConstType =>
    typeof (parameter as PlatformConstType).PlatformConst === 'object';

export const isConst = (parameter: ParameterType): parameter is ConstType =>
    typeof (parameter as ConstType).Const === 'string';
