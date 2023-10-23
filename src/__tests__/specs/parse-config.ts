import { parseConfigFile } from '../../parsers/yaml-parser';

describe('parse config', () => {
    it('simple parse yaml config', async () => {
        expect(await parseConfigFile('src/__tests__/examples/evgen.yaml')).toMatchSnapshot();
    });
});
