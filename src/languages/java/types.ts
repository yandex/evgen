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
            return elementType ? `List<${primitiveTypeFormat(elementType)}>` : 'List';
        case 'Dict':
            return `Map<String, ${elementType ? primitiveTypeFormat(elementType) : '?'}>`;
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
        return primitiveType.Enum.name || '?';
    }
    switch (primitiveType) {
        case 'String':
            return 'String';
        case 'Int':
            return 'int';
        case 'Long Int':
            return 'long';
        case 'Double':
            return 'double';
        case 'Bool':
            return 'boolean';
        case 'TimeMilliseconds':
            return 'long';
        case 'Dict':
            return 'Map<String, ?>';
        case 'List':
            return 'List';
        default:
            throw new Error(`Unknown type: ${JSON.stringify(primitiveType)}`);
    }
};
