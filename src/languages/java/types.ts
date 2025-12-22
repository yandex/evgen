import { PrimitiveType, SinglePlatformParameterType } from '../../types/data-types';
import { EventParameter, GlobalType } from '../../types/parsed-types';
import {
    pascalCase,
    isEnum,
    isConst,
    isTypedDict,
    isTypedList,
    isCustomParameter,
    isRef,
    extractRef,
} from '../../helpers';

interface TypeFormatOptions {
    globalTypes?: Record<string, GlobalType>;
}

export const typeFormat = (
    parameter: EventParameter<SinglePlatformParameterType>,
    options: TypeFormatOptions = {}
): string => {
    const { type, elementType, name, namespace, version } = parameter;
    const { globalTypes = {} } = options;

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
            // Вместо typealias-конструкций резолвим тип инлайн
            if (isRef(type)) {
                const refName = extractRef(type);
                const globalType = globalTypes[refName];
                if (globalType) {
                    return typeFormat(
                        {
                            ...parameter,
                            type: globalType.type as SinglePlatformParameterType,
                        },
                        options
                    );
                }
                return pascalCase(refName);
            }
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
                return pascalCase(type.name || name);
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
        case 'TimeMilliseconds':
            return 'long';
        case 'Double':
            return 'double';
        case 'Bool':
            return 'boolean';
        case 'Dict':
            return 'Map<String, ?>';
        case 'List':
            return 'List';
        default:
            throw new Error(`Unknown type: ${JSON.stringify(primitiveType)}`);
    }
};
