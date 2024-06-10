import { PrimitiveType, SinglePlatformParameterType } from '../../types/data-types';
import { EventParameter } from '../../types/parsed-types';
import { pascalCase, isEnum, isConst, isTypedDict, isTypedList } from '../../helpers';

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
            return `Dictionary<string, ${
                elementType ? primitiveTypeFormat(elementType) : 'object'
            }>`;
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
            throw new Error(`Unknown type: ${JSON.stringify(type)}`);
    }
};

export const primitiveTypeFormat = (primitiveType: PrimitiveType): string => {
    if (isEnum(primitiveType)) {
        return primitiveType.Enum.name || 'object';
    }
    switch (primitiveType) {
        case 'String':
            return 'string';
        case 'Int':
            return 'int';
        case 'Long Int':
            return 'long';
        case 'Double':
            return 'double';
        case 'Bool':
            return 'bool';
        case 'TimeMilliseconds':
            return 'ulong';
        case 'Dict':
            return 'Dictionary<string, object>';
        case 'List':
            return 'List<object>';
        default:
            throw new Error(`Unknown type: ${JSON.stringify(primitiveType)}`);
    }
};
