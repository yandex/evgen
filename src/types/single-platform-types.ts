import { SinglePlatformParameterType } from './data-types';
import {
    EventNamespace,
    GlobalParameters,
    EventParameter,
    InterfaceVersion,
    EventData,
    Event,
} from './parsed-types';

export interface SinglePlatformNamespaceCollection {
    globalParameters: SinglePlatformGlobalParameters;
    platformParameters: SinglePlatformParameters;
    eventNamespaces: EventNamespace<SinglePlatformEvent>[];
}

export interface SinglePlatformGlobalParameters extends GlobalParameters {
    parameters: EventParameter<SinglePlatformParameterType>[];
}

export interface SinglePlatformParameters {
    parameters: EventParameter<SinglePlatformParameterType>[];
}

export interface SinglePlatformInterfaceVersion extends InterfaceVersion {
    parameters: EventParameter<SinglePlatformParameterType>[];
}

export interface SinglePlatformEvent extends Event {
    versions: SinglePlatformEventVersion[];
}

export interface SinglePlatformEventVersion extends EventData {
    platform: string;
    parameters: EventParameter<SinglePlatformParameterType>[];
}
