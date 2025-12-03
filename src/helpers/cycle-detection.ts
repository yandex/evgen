import { logger } from './logger';

export type CycleTracker = WeakMap<object, number>;

export const createCycleTracker = (): CycleTracker => new WeakMap();

export const assertNoCycle = (node: object, path: string[], visited: CycleTracker): void => {
    if (visited.has(node)) {
        const cycleStart = visited.get(node)!;
        const pathBefore = path.slice(0, cycleStart);
        const cycle = path.slice(cycleStart);
        logger.error(
            'Circular structure detected.\n' +
                `  Path: ${pathBefore.join(' -> ') || '(root)'}\n` +
                `  Cycle: ${cycle.join(' -> ')} -> [${cycle[0]}]`
        );
        process.exit(1);
    }
};

export const markVisited = (node: object, path: string[], visited: CycleTracker): void => {
    visited.set(node, path.length);
};

export const unmarkVisited = (node: object, visited: CycleTracker): void => {
    visited.delete(node);
};
