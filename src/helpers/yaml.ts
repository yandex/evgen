import { stringify } from 'yaml';

const STRINGIFY_OPTIONS = {
    // 1.1 строже: `yes`, `off` и `12:30` получат кавычки и останутся строками.
    version: '1.1' as const,
    // Блочный скаляр занял бы несколько строк и сломал вёрстку шаблона.
    blockQuote: false,
    lineWidth: 0,
};

export const yamlScalar = (value: unknown) => stringify(value, STRINGIFY_OPTIONS).trimEnd();
