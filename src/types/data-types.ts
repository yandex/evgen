export type ConstType = { Const: string };

export type PlatformConstType = { PlatformConst: Record<string, string> };

export type EnumType = {
    Enum: {
        name?: string;
        values: number[] | string[];
    };
};

export type PrimitiveType =
    | 'String'
    | 'Int'
    | 'Long Int'
    | 'Bool'
    | 'Double'
    | 'TimeMilliseconds'
    | 'Dict'
    | 'List'
    | EnumType;

export type SinglePlatformParameterType = PrimitiveType | ConstType;

export type ParameterType = SinglePlatformParameterType | PlatformConstType;
