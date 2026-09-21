import { mkdtemp, readFile, rm } from 'fs/promises';
import { tmpdir } from 'os';
import { join, resolve } from 'path';

import { parse as yamlParse } from 'yaml';

import { generateEventsDocs } from '../../evgen';
import { parseEvents } from '../../parsers';
import { parseEventsFile } from '../../parsers/yaml-parser';
import { RawEvents } from '../../types/raw-types';

const EVENTS_PATH = 'src/__tests__/examples/yaml-doc-defaults';
const TEMPLATE_DIR = resolve(__dirname, '../../templates/yaml');

const generateYamlDoc = async () => {
    const outputPath = await mkdtemp(join(tmpdir(), 'evgen-yaml-doc-'));
    try {
        const rawEvents = await parseEventsFile(EVENTS_PATH);
        await generateEventsDocs(parseEvents(rawEvents as RawEvents), {
            outputPath,
            templateDir: TEMPLATE_DIR,
        });
        return await readFile(join(outputPath, 'all_events.yaml'), 'utf-8');
    } finally {
        await rm(outputPath, { recursive: true, force: true });
    }
};

describe('generate yaml doc', () => {
    let doc: string;
    let globalParams: Record<string, { default_value?: unknown }>;

    beforeAll(async () => {
        doc = await generateYamlDoc();
        globalParams = yamlParse(doc)['.GlobalParams'].parameters;
    });

    it('produces parsable yaml', () => {
        expect(() => yamlParse(doc)).not.toThrow();
    });

    it.each([
        ['dash', '-'],
        ['negativeNumberString', '-1'],
        ['emptyString', ''],
        ['zero', 0],
        ['falseFlag', false],
        ['boolString', 'False'],
        ['yesString', 'yes'],
        ['colonString', '12:30'],
        ['plainString', 'unknown'],
    ])('keeps default value of %s intact', (name, expected) => {
        expect(globalParams[name].default_value).toBe(expected);
    });

    it('omits default_value for optional parameter without one', () => {
        expect(globalParams.optionalWithoutDefault).not.toHaveProperty('default_value');
    });

    it('matches snapshot', () => {
        expect(doc).toMatchSnapshot();
    });
});
