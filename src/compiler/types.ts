import Hbs from 'handlebars';
import type { CaseMode, CodeLanguage } from '../types/evgen-config';

export type Handlebars = typeof Hbs;

export interface CompileOptions {
    outputPath: string;
    templateDir: string;
    language?: CodeLanguage;
    paramNameCase?: CaseMode;
}
