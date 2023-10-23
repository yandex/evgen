import { ParameterType } from '../types/data-types';
import { EventVersion, EventParameter, InterfaceVersion } from '../types/parsed-types';

export const getLatestCompatibleVersion = (
    eventVersion: EventVersion,
    interfaces: InterfaceVersion[],
    globalParameters: EventParameter<ParameterType>[]
) => {
    const descSortedInterfaces = interfaces.sort((i1, i2) => i2.version - i1.version);
    const latestCompatible = descSortedInterfaces.find((interfaceVersion) => {
        const compatibility = checkCompatible(eventVersion, interfaceVersion, globalParameters);
        return compatibility.isCompatible;
    });

    return latestCompatible?.version;
};

interface CompatibilityResult {
    isInProd: boolean;
    isCompatible: boolean;
    diff: EventParameter<ParameterType>[];
}

const checkCompatible = (
    eventVersion: EventVersion,
    iface: InterfaceVersion,
    globalParameters: EventParameter<ParameterType>[]
) => {
    const isInProd = eventVersion.platforms
        ? Object.values(eventVersion.platforms).some((platform) => platform.lastVersion !== null)
        : false;

    const result: CompatibilityResult = { isInProd, isCompatible: true, diff: [] };
    iface.parameters.forEach((ifaceParameter) => {
        const isCompatible =
            eventVersion.parameters.some((eventParameter) =>
                isParameterCompatible(eventParameter, ifaceParameter)
            ) ||
            globalParameters.some((globalParameter) =>
                isParameterCompatible(globalParameter, ifaceParameter)
            );
        if (!isCompatible) {
            result.isCompatible = false;
            result.diff.push(ifaceParameter);
        }
    });

    return result;
};

const isParameterCompatible = (
    param1: EventParameter<ParameterType>,
    param2: EventParameter<ParameterType>
) => param1.name === param2.name;
