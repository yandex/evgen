export type ConstType = { Const: string };

export type PlatformConstType = { PlatformConst: Record<string, string> };

export type EnumType = {
    Enum: {
        name?: string;
        values: number[] | string[];
    };
};

export type TypedDict = {
    Dict: { [k: string]: PrimitiveType };
};

export type TypedList = {
    List: { [k: string]: PrimitiveType };
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

export type SinglePlatformParameterType = PrimitiveType | ConstType | TypedDict | TypedList;

export type ParameterType = SinglePlatformParameterType | PlatformConstType;
