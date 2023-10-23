import { parseEventsFile } from '../../parsers/yaml-parser';

describe('parse event yaml file', () => {
    it('parse simple yaml', async () => {
        expect(await parseEventsFile('src/__tests__/examples/events.yaml')).toMatchSnapshot();
    });
});
