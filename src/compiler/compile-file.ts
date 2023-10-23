import { mkdir, readFile, writeFile } from 'fs/promises';
import { dirname, resolve } from 'path';

import Hbs from 'handlebars';

import { parseInlineFiles } from './parse-inline-files';
import { TEMPLATE_EXTENSION } from './constants';
import { Handlebars } from './types';

interface CompileFileOptions {
    outputPath: string;
    templateDir: string;
    hbs?: Handlebars;
}

export const compileFile = async (
    templateRelativePath: string,
    ctx: Record<string, unknown>,
    options: CompileFileOptions
) => {
    const { templateDir, outputPath, hbs = Hbs } = options;

    const fileRealRelativePath = hbs.compile(decodeURIComponent(templateRelativePath))(ctx);
    const templatePath = resolve(templateDir, templateRelativePath);
    const templateStr = await readFile(templatePath, { encoding: 'utf-8' });

    const template = hbs.compile(templateStr, { noEscape: true });
    const initialFile = resolve(
        outputPath,
        fileRealRelativePath.replace(`.${TEMPLATE_EXTENSION}`, '')
    );

    const compiledStr = template(ctx);
    const inlineFiles = parseInlineFiles(compiledStr, initialFile);

    return Object.keys(inlineFiles)
        .filter((file) => inlineFiles[file] && !inlineFiles[file].match(/^\s+$/g))
        .map(async (filePath) => {
            const fileDir = dirname(filePath);
            await mkdir(fileDir, { recursive: true });

            return writeFile(filePath, inlineFiles[filePath]);
        });
};
