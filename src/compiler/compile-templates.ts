import { join } from 'path';

import fg from 'fast-glob';

import { CodeLanguage } from '../types/evgen-config';

import { PARTIALS_DIR, TEMPLATE_EXTENSION } from './constants';
import { createHandlebars } from './create-compiler';
import { compileFile } from './compile-file';

interface CompileOptions {
    language?: CodeLanguage;
    outputPath: string;
    templateDir: string;
}

export const compileTemplates = async (ctx: Record<string, unknown>, options: CompileOptions) => {
    const { templateDir, language, outputPath } = options;
    const partialsDir = join(templateDir, PARTIALS_DIR);
    const hbs = await createHandlebars({ language, partialsDir });

    const templateRelativePaths = await fg(`**/*.${TEMPLATE_EXTENSION}`, {
        cwd: templateDir,
        ignore: [`${PARTIALS_DIR}/**`],
    });

    if (!templateRelativePaths.length) {
        console.log(`Skip generate to ${outputPath}. No templates found in ${templateDir}.`);
    }

    return Promise.all(
        templateRelativePaths.map(async (templateRelativePath) =>
            compileFile(templateRelativePath, ctx, {
                hbs,
                templateDir,
                outputPath,
            })
        )
    );
};
