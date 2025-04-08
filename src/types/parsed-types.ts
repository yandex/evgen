import { ParameterType, PrimitiveType } from './data-types';

export interface NamespaceCollection {
    globalParameters?: GlobalParameters;
    platformParameters: Record<string, PlatformParameters>;
    eventNamespaces: EventNamespace<Event>[];
    interfaceNamespaces: Record<string, InterfaceVersion[]>;
    shared: unknown;
}

export interface GlobalParameters {
    parameters: EventParameter<ParameterType>[];
    description: string;
    comment?: string;
}

export interface PlatformParameters {
    parameters: EventParameter<ParameterType>[];
    description: string;
    comment?: string;
}

export interface EventNamespace<T> {
    name: string;
    events: T[];
    documentationDir?: string;
}

export interface InterfaceVersion {
    name: string;
    namespace: string;
    version: number;
    parameters: EventParameter<ParameterType>[];
    description: string;
}

export interface Event {
    name: string;
    versions: EventVersion[];
}

export interface EventData {
    event: string;
    name: string;
    namespace: string;
    additionalNamespaces: string[];
    version: number;
    description: string;
    interfaces: Record<string, number>;
    comment?: string;
    interfaceNames?: string[];
    tags: string[];
}

export interface EventVersion extends EventData {
    platforms?: Record<string, Platform>;
    parameters: EventParameter<ParameterType>[];
}

export interface EventParameter<T> {
    name: string;
    namespace: string;
    version: number;
    type: T;
    description: string;
    abstract: boolean;
    optional: boolean;
    elementType?: PrimitiveType;
    defaultValue?: string;
}

export interface Platform {
    name: string;
    firstVersion: string;
    lastVersion: string | null;
    ticket?: string;
}
