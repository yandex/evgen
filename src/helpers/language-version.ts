const LANGUAGE_VERSION_FORMAT = /^\d+(\.\d+)*$/;

export const resolveLanguageVersion = (value: unknown): string | undefined => {
    if (value === undefined || value === null) {
        return undefined;
    }
    const languageVersion = typeof value === 'number' ? String(value) : value;
    if (typeof languageVersion !== 'string' || !LANGUAGE_VERSION_FORMAT.test(languageVersion)) {
        throw new Error(
            `Unsupported language_version: ${JSON.stringify(value)}. ` +
                'Expected a version number such as "6" or "6.0"'
        );
    }
    return languageVersion;
};

export const majorLanguageVersion = (languageVersion?: string): number | undefined =>
    languageVersion === undefined ? undefined : Number(languageVersion.split('.')[0]);
