import { PlatformParameters } from '../types/parsed-types';
import { RawPlatformParameters } from '../types/raw-types';

import { parseParameters } from './event-parameters';

export const parsePlatformParameters = (
    rawPlatformParametersSet: Record<string, RawPlatformParameters>
): Record<string, PlatformParameters> => {
    const platformParameters: Record<string, PlatformParameters> = {};
    Object.entries(rawPlatformParametersSet).forEach(([platformName, rawPlatformParameters]) => {
        platformParameters[platformName] = {
            description: rawPlatformParameters.description,
            parameters: parseParameters(rawPlatformParameters.parameters),
            comment: rawPlatformParameters.comment,
        };
    });

    return platformParameters;
};
