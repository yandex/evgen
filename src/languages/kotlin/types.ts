import { PrimitiveType, SinglePlatformParameterType } from '../../types/data-types';
import { EventParameter } from '../../types/parsed-types';
import {
    pascalCase,
    isEnum,
    isConst,
    isTypedDict,
    isTypedList,
    isCustomParameter,
} from '../../helpers';

export const typeFormat = (parameter: EventParameter<SinglePlatformParameterType>): string => {
    const { type, elementType, name, namespace, version } = parameter;
    switch (type) {
        case 'String':
        case 'Int':
        case 'Long Int':
        case 'Double':
        case 'Bool':
        case 'TimeMilliseconds':
            return primitiveTypeFormat(type);
        case 'List':
            return `List<${elementType ? primitiveTypeFormat(elementType) : ''}>`;
        case 'Dict':
            return `Map<String, ${elementType ? primitiveTypeFormat(elementType) : 'Any'}>`;
        default:
            if (isEnum(type)) {
                return (
                    type.Enum.name ||
                    namespace + (version > 1 ? `V${version}` : '') + pascalCase(name)
                );
            }
            if (isConst(type)) {
                return `'${type.Const}'`;
            }
            if (isTypedList(type)) {
                return primitiveTypeFormat('List');
            }
            if (isTypedDict(type)) {
                return primitiveTypeFormat('Dict');
            }
            if (isCustomParameter(type)) {
                return pascalCase(name);
            }
            throw new Error(`Unknown type: ${JSON.stringify(type)}`);
    }
};

export const primitiveTypeFormat = (primitiveType: PrimitiveType): string => {
    if (isEnum(primitiveType)) {
        return primitiveType.Enum.name || 'Any';
    }
    switch (primitiveType) {
        case 'String':
            return 'String';
        case 'Int':
            return 'Int';
        case 'Long Int':
            return 'Long';
        case 'Double':
            return 'Double';
        case 'Bool':
            return 'Boolean';
        case 'TimeMilliseconds':
            return 'Long';
        case 'Dict':
            return 'Map<String, Any>';
        case 'List':
            return 'List<Any>';
        default:
            throw new Error(`Unknown type: ${JSON.stringify(primitiveType)}`);
    }
};
