import Hbs from 'handlebars';

import type { CompileOptions } from './types';

import { TEMPLATE_EXTENSION } from './constants';
import { registerHelpers } from './register-helpers';
import { registerPartials } from './register-partials';

interface CreateHandlebarsOptions {
    compileOptions: CompileOptions;
    partialsDir?: string;
    extension?: string;
}

export const createHandlebars = async ({
    compileOptions,
    partialsDir,
    extension = TEMPLATE_EXTENSION,
}: CreateHandlebarsOptions) => {
    const hbs = Hbs.create();
    registerHelpers(hbs, compileOptions);

    if (partialsDir) {
        await registerPartials(hbs, partialsDir, {
            extension,
        });
    }

    return hbs;
};
