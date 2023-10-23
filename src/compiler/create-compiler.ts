import Hbs from 'handlebars';

import { CodeLanguage } from '../types/evgen-config';

import { TEMPLATE_EXTENSION } from './constants';
import { registerHelpers } from './register-helpers';
import { registerPartials } from './register-partials';

interface CreateHandlebarsOptions {
    language?: CodeLanguage;
    partialsDir?: string;
    extension?: string;
}

export const createHandlebars = async ({
    language,
    partialsDir,
    extension = TEMPLATE_EXTENSION,
}: CreateHandlebarsOptions) => {
    const hbs = Hbs.create();
    registerHelpers(hbs, language);

    if (partialsDir) {
        await registerPartials(hbs, partialsDir, {
            extension,
        });
    }

    return hbs;
};
