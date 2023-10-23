module.exports = {
    parser: '@typescript-eslint/parser',
    extends: ['plugin:@typescript-eslint/recommended', 'prettier'],
    plugins: ['prettier'],
    parserOptions: {
        ecmaVersion: 2018,
        sourceType: 'module',
    },
    rules: {
        'prettier/prettier': ['error'],
        'no-param-reassign': 'off',
        'no-console': 'off',
    },
    ignorePatterns: ['dist/', 'tutorial/', 'demo/'],
    settings: {
        jest: {
            version: 26,
        },
    },
};
