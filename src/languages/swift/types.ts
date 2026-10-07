import { PrimitiveType, SinglePlatformParameterType } from '../../types/data-types';
import { EventParameter } from '../../types/parsed-types';
import {
    pascalCase,
    isEnum,
    isConst,
    isTypedDict,
    isTypedList,
    isCustomParameter,
    isRef,
    extractRef,
    majorLanguageVersion,
} from '../../helpers';

const SENDABLE_MIN_SWIFT_VERSION = 6;

export const isSendableMode = (languageVersion?: string): boolean =>
    (majorLanguageVersion(languageVersion) ?? 0) >= SENDABLE_MIN_SWIFT_VERSION;

export const anyType = (languageVersion?: string): string =>
    isSendableMode(languageVersion) ? 'any Sendable' : 'Any';

interface TypeFormatOptions {
    languageVersion?: string;
}

export const typeFormat = (
    parameter: EventParameter<SinglePlatformParameterType>,
    { languageVersion }: TypeFormatOptions = {}
): string => {
    const { type, elementType, namespace, version, name } = parameter;
    const valueType = anyType(languageVersion);
    switch (type) {
        case 'String':
        case 'Int':
        case 'Long Int':
        case 'Double':
        case 'Bool':
        case 'TimeMilliseconds':
            return primitiveTypeFormat(type, valueType);
        case 'List':
            return `[${elementType ? primitiveTypeFormat(elementType, valueType) : ''}]`;
        case 'Dict':
            return `[String: ${
                elementType ? primitiveTypeFormat(elementType, valueType) : valueType
            }]`;
        default:
            if (isRef(type)) {
                return pascalCase(extractRef(type));
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
                return primitiveTypeFormat('List', valueType);
            }
            if (isTypedDict(type)) {
                return primitiveTypeFormat('Dict', valueType);
            }
            if (isCustomParameter(type)) {
                return primitiveTypeFormat(type, valueType);
            }
            throw new Error(`Unknown type: ${JSON.stringify(type)}`);
    }
};

const primitiveTypeFormat = (primitiveType: PrimitiveType, valueType: string): string => {
    if (isEnum(primitiveType)) {
        return primitiveType.Enum.name || valueType;
    }
    if (isCustomParameter(primitiveType)) {
        return pascalCase(primitiveType.name);
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
            return `[String: ${valueType}]`;
        case 'List':
            return `[${valueType}]`;
        default:
            throw new Error(`Unknown type: ${JSON.stringify(primitiveType)}`);
    }
};
