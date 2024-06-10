export interface Config {
    code: Record<string, CodeConfig>;
    doc: Record<string, DocConfig>;
}

export type CodeLanguage = 'kotlin' | 'swift' | 'type_script' | 'java' | 'c_sharp';

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
