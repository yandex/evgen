import { join } from 'path';
import fg from 'fast-glob';

import type { CompileOptions } from './types';
import { PARTIALS_DIR, TEMPLATE_EXTENSION } from './constants';
import { createHandlebars } from './create-compiler';
import { compileFile } from './compile-file';

export const compileTemplates = async (ctx: Record<string, unknown>, options: CompileOptions) => {
    const { templateDir, outputPath } = options;
    const partialsDir = join(templateDir, PARTIALS_DIR);
    const hbs = await createHandlebars({ partialsDir, compileOptions: options });

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
