import { PrimitiveType, SinglePlatformParameterType } from '../../types/data-types';
import { EventParameter } from '../../types/parsed-types';
import { pascalCase, isEnum, isConst, isTypedDict, isTypedList } from '../../helpers';

export const typeFormat = (parameter: EventParameter<SinglePlatformParameterType>): string => {
    const { type, elementType, namespace, version, name } = parameter;
    switch (type) {
        case 'String':
        case 'Int':
        case 'Long Int':
        case 'Double':
        case 'Bool':
        case 'TimeMilliseconds':
            return primitiveTypeFormat(type);
        case 'List':
            return `[${elementType ? primitiveTypeFormat(elementType) : ''}]`;
        case 'Dict':
            return `[String: ${elementType ? primitiveTypeFormat(elementType) : 'Any'}]`;
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

const primitiveTypeFormat = (primitiveType: PrimitiveType): string => {
    if (isEnum(primitiveType)) {
        return primitiveType.Enum.name || 'Any';
    }
    switch (primitiveType) {
        case 'String':
            return 'String';
        case 'Int':
        case 'Long Int':
            return 'Int';
        case 'Double':
            return 'Double';
        case 'Bool':
            return 'Bool';
        case 'TimeMilliseconds':
            return 'Double';
        case 'Dict':
            return '[String: Any]';
        case 'List':
            return '[Any]';
        default:
            throw new Error(`Unknown type: ${JSON.stringify(primitiveType)}`);
    }
};
