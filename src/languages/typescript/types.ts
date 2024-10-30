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
            return `${elementType ? primitiveTypeFormat(elementType) : ''}[]`;
        case 'Dict':
            return `Record<string, ${elementType ? primitiveTypeFormat(elementType) : 'any'}>`;
        default:
            if (isEnum(type)) {
                return (
                    type.Enum.name ||
                    namespace + (version > 1 ? `V${version}` : '') + pascalCase(name)
                );
            }
            if (isConst(type)) {
                return `"${type.Const}"`;
            }
            if (isTypedList(type)) {
                return `{ ${Object.entries(type.List)
                    .map(
                        ([key, value]) =>
                            `${key}: ${typeFormat({
                                ...parameter,
                                elementType: undefined,
                                type: value,
                            })};`
                    )
                    .join(' ')} }[]`;
            }
            if (isTypedDict(type)) {
                return `{ ${Object.entries(type.Dict)
                    .map(
                        ([key, value]) =>
                            `${key}: ${typeFormat({
                                ...parameter,
                                elementType: undefined,
                                type: value,
                            })};`
                    )
                    .join(' ')} }`;
            }
            if (isCustomParameter(type)) {
                return pascalCase(name);
            }
            throw new Error(`Unknown type: ${JSON.stringify(type)}`);
    }
};

const primitiveTypeFormat = (primitiveType: PrimitiveType): string => {
    if (isEnum(primitiveType)) {
        return primitiveType.Enum.name || 'any';
    }
    switch (primitiveType) {
        case 'String':
            return 'string';
        case 'Int':
        case 'Long Int':
        case 'Double':
            return 'number';
        case 'Bool':
            return 'boolean';
        case 'TimeMilliseconds':
            return 'number';
        case 'Dict':
            return 'Record<string, any>';
        case 'List':
            return 'any[]';
        default:
            throw new Error(`Unknown type: ${JSON.stringify(primitiveType)}`);
    }
};
