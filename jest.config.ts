export default {
    collectCoverageFrom: [
        '**/*.{ts,tsx,js,jsx,}',
        '!**/@types/**',
        '!**/*.d.ts',
        '!**/build/**',
        '!**/dist/**',
        '!**/node_modules/**',
        '!**/typings/**',
    ],
    coverageReporters: ['json', 'html', 'lcovonly', 'text-summary', 'clover'],
    cacheDirectory: '<rootDir>/.jest/.cache',
    coverageDirectory: '<rootDir>/.jest/.coverage',
    moduleFileExtensions: ['ts', 'js', 'json'],
    modulePaths: ['<rootDir>'],
    reporters: [
        'default',
        [
            'jest-html-reporters',
            {
                publicPath: '.jest/.report',
                filename: 'index.html',
            },
        ],
    ],
    testEnvironment: 'node',
    testPathIgnorePatterns: ['/node_modules/', '<rootDir>/build/', '<rootDir>/dist/'],
    testMatch: ['**/__tests__/**/specs/*.[jt]s'],
    rootDir: './src',
};
