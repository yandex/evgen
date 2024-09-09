export interface Config {
    code: Record<string, CodeConfig>;
    doc: Record<string, DocConfig>;
    options?: EvgenOptions;
}

export type CodeLanguage = 'kotlin' | 'swift' | 'type_script' | 'java' | 'dart' | 'c_sharp';

export type DocsType = 'txt' | 'md' | 'yaml';

export interface CodeConfig {
    platform: string;
    output_dir: string;
    language: CodeLanguage;
    class_name: string;
    only_last_version?: boolean;
    param_name_case?: string;
    template_dir?: string;
}

export interface DocConfig {
    extension: DocsType;
    output_dir: string;
    template_dir?: string;
}

interface EvgenOptions {
    /**
     * Keep order of fields included via '_included' field prefix.
     *
     * False (default) - Originally '_included' fields were before other fields in generated code and documentation. It was done for compatibility with previous version of EvGen
     * True - order according to yaml spec
     */
    keepParametersOrder: boolean;
}
