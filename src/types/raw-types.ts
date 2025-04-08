import {
    EVENTS_FIELD,
    GLOBAL_PARAMETERS_FIELD,
    SHARED_FIELD,
    INTERFACES_FIELD,
    PLATFORM_PARAMETERS_FIELD,
} from '../parsers/constants';

import { ParameterType, PrimitiveType } from './data-types';

export interface RawPlatform {
    app_versions: string | number;
    ticket?: string;
}

export interface RawEventParameter {
    type: ParameterType;
    description?: string;
    default_value?: string;
    abstract?: boolean;
    optional?: boolean;
    element_type?: PrimitiveType;
}

export interface RawEvent {
    parameters: Record<string, RawEventParameter> | null;
    description: string;
    platforms?: Record<string, RawPlatform>;
    comment?: string;
    interface?: string | string[];
    namespaces?: string[];
    force_event_name?: string;
    tags?: string | string[];
}

export interface RawGlobalParameters {
    parameters: Record<string, RawEventParameter> | null;
    description: string;
    comment?: string;
    platforms?: Record<string, RawPlatform>;
}

export interface RawPlatformParameters {
    parameters: Record<string, RawEventParameter> | null;
    description: string;
    comment?: string;
}

export interface RawInterface {
    description?: string;
    parameters: Record<string, RawEventParameter>;
}

export type NestedRecord<T> = T | Record<string, T>;

export interface RawEvents {
    [GLOBAL_PARAMETERS_FIELD]: RawGlobalParameters;
    [PLATFORM_PARAMETERS_FIELD]?: Record<string, RawPlatformParameters>;
    [EVENTS_FIELD]: Record<string, NestedRecord<NestedRecord<RawEvent>>>;
    [INTERFACES_FIELD]?: Record<string, NestedRecord<NestedRecord<RawInterface>>>;
    [SHARED_FIELD]?: unknown;
}
