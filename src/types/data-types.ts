export type ConstType = { Const: string };

export type PlatformConstType = { PlatformConst: Record<string, string> };

type ValueWithDescription = {
    value: number | string;
    description?: string;
};

export type EnumType = {
    Enum: {
        name?: string;
        values: ValueWithDescription[] | number[] | string[];
    };
};

export type TypedDict = {
    Dict: { [k: string]: PrimitiveType };
};

export type TypedList = {
    List: { [k: string]: PrimitiveType };
};

export type CustomType = {
    name: string;
    isNamed: boolean;
    Custom: unknown;
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
    | EnumType
    | CustomType;

export type SinglePlatformParameterType = PrimitiveType | ConstType | TypedDict | TypedList;

export type ParameterType = SinglePlatformParameterType | PlatformConstType;
