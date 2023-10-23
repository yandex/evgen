import { isObject } from 'lodash';

import { GlobalParameters } from '../types/parsed-types';
import { RawGlobalParameters } from '../types/raw-types';

import { GLOBAL_PARAMETERS_FIELD } from './constants';
import { parseParameters } from './event-parameters';

export const parseGlobalParameters = (
    rawGlobalParameters: RawGlobalParameters
): GlobalParameters => {
    if (!rawGlobalParameters) {
        throw new Error(`Could not find definition of ${GLOBAL_PARAMETERS_FIELD}`);
    }

    if (!isObject(rawGlobalParameters)) {
        throw new Error(
            `Expected global parameters to be an object, but got ${typeof rawGlobalParameters}`
        );
    }

    const parameters = parseParameters(rawGlobalParameters.parameters);

    return {
        parameters,
        description: rawGlobalParameters.description,
        comment: rawGlobalParameters.comment,
    };
};
