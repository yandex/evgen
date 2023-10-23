export const entries = (obj: unknown) => {
    if (!obj || typeof obj !== 'object') {
        return [];
    }

    return Object.entries(obj).map(([key, value]) => ({ key, value }));
};
