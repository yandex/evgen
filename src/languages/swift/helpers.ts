import { SinglePlatformParameterType } from '../../types/data-types';
import { EventParameter } from '../../types/parsed-types';

import { anyType, isSendableMode, typeFormat } from './types';

interface TemplateOptions {
    data?: { root?: { languageVersion?: string } };
}

const languageVersionOf = (options?: TemplateOptions) => options?.data?.root?.languageVersion;

export const swiftHelpers = {
    typeFormat: (
        parameter: EventParameter<SinglePlatformParameterType>,
        options?: TemplateOptions
    ) => typeFormat(parameter, { languageVersion: languageVersionOf(options) }),
    anyType: (options?: TemplateOptions) => anyType(languageVersionOf(options)),
    isSendableMode: (options?: TemplateOptions) => isSendableMode(languageVersionOf(options)),
};
