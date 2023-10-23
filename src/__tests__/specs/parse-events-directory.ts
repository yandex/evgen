import { parseEventsFile } from '../../parsers/yaml-parser';

describe('parse event yaml directory', () => {
    it('parse events directory yaml with includes', async () => {
        expect(await parseEventsFile('src/__tests__/examples/events')).toMatchSnapshot();
    });
});
