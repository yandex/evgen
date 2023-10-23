import { resolve } from 'path';
import { readFile } from 'fs/promises';

import fg from 'fast-glob';

import { Handlebars } from './types';
import { TEMPLATE_EXTENSION } from './constants';

export const registerPartials = async (
    hbs: Handlebars,
    partialsDir: string,
    { extension = TEMPLATE_EXTENSION }
) => {
    const partialsTemplates = await fg(`*.${extension}`, {
        cwd: partialsDir,
    });

    return Promise.all(
        partialsTemplates.map(async (path) => {
            const absolutePath = resolve(partialsDir, path);
            const templateStr = await readFile(absolutePath, { encoding: 'utf-8' });
            const partialName = path.replace(`.${extension}`, '');
            hbs.registerPartial(partialName, templateStr);
        })
    );
};
