const colors = {
    reset: '\x1b[0m',
    bold: '\x1b[1m',

    red: '\x1b[31m',
    yellow: '\x1b[33m',
    cyan: '\x1b[36m',
} as const;

const formatMessage = (prefix: string, color: string, ...args: unknown[]): string[] => {
    const formattedPrefix = `${color}${colors.bold}${prefix}${colors.reset}`;
    return [formattedPrefix, ...args.map(String)];
};

export const logger = {
    error: (...args: unknown[]): void => {
        console.error(...formatMessage('ERROR:', colors.red, ...args));
    },

    warn: (...args: unknown[]): void => {
        console.warn(...formatMessage('WARN:', colors.yellow, ...args));
    },

    info: (...args: unknown[]): void => {
        console.info(...formatMessage('INFO:', colors.cyan, ...args));
    },
};
