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

export const primitiveTypeFormat = (primitiveType: PrimitiveType): string =>
    primitiveTypeFormatInternal(primitiveType, false);

export const nullablePrimitiveTypeFormat = (primitiveType: PrimitiveType): string =>
    primitiveTypeFormatInternal(primitiveType, true);

const typeFormatInternal = (
    parameter: EventParameter<SinglePlatformParameterType>,
    options: TypeFormatOptions,
    nullable: boolean
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
            return primitiveTypeFormatInternal(type, nullable);
        case 'List':
            return elementType
                ? `List<${primitiveTypeFormatInternal(elementType, false)}>`
                : 'List';
        case 'Dict':
            return `Map<String, ${
                elementType ? primitiveTypeFormatInternal(elementType, false) : '?'
            }>`;
        default:
            if (isRef(type)) {
                const refName = extractRef(type);
                const globalType = globalTypes[refName];
                if (globalType) {
                    return typeFormatInternal(
                        {
                            ...parameter,
                            type: globalType.type as SinglePlatformParameterType,
                        },
                        options,
                        nullable
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
                return primitiveTypeFormatInternal('List', nullable);
            }
            if (isTypedDict(type)) {
                return primitiveTypeFormatInternal('Dict', nullable);
            }
            if (isCustomParameter(type)) {
                return pascalCase(type.name || name);
            }
            throw new Error(`Unknown type: ${JSON.stringify(type)}`);
    }
};

const primitiveTypeFormatInternal = (primitiveType: PrimitiveType, nullable: boolean): string => {
    if (isEnum(primitiveType)) {
        return primitiveType.Enum.name || '?';
    }

    switch (primitiveType) {
        case 'String':
            return 'String';
        case 'Int':
            return nullable ? 'Integer' : 'int';
        case 'Long Int':
        case 'TimeMilliseconds':
            return nullable ? 'Long' : 'long';
        case 'Double':
            return nullable ? 'Double' : 'double';
        case 'Bool':
            return nullable ? 'Boolean' : 'boolean';
        case 'Dict':
            return 'Map<String, ?>';
        case 'List':
            return 'List';
        default:
            throw new Error(`Unknown type: ${JSON.stringify(primitiveType)}`);
    }
};

export const typeFormat = (
    parameter: EventParameter<SinglePlatformParameterType>,
    options: TypeFormatOptions = {}
): string => typeFormatInternal(parameter, options, false);

export const nullableTypeFormat = (
    parameter: EventParameter<SinglePlatformParameterType>,
    options: TypeFormatOptions = {}
): string => typeFormatInternal(parameter, options, true);
