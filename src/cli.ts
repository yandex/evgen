#!/usr/bin/env node
import { resolve, join, dirname } from 'path';

import { Command } from 'commander';
import { cloneDeep } from 'lodash';

import { generateEventsCode, generateEventsDocs } from './evgen';
import { parseConfigFile, parseEventsFile } from './parsers/yaml-parser';
import { parseEvents } from './parsers';
import { CodeLanguage, Config, DocsType } from './types/evgen-config';
import { RawEvents } from './types/raw-types';
import { singlePlatformEvents } from './parsers/single-platform-events';
import { logger } from './helpers';

const program = new Command();

const DEFAULT_TEMPLATES_PATH = resolve(__dirname, 'templates');
const DEFAULT_TEMPLATES_DIRS: Record<CodeLanguage | DocsType, string> = {
    type_script: 'typescript',
    kotlin: 'kotlin',
    swift: 'swift',
    java: 'java',
    dart: 'dart',
    c_sharp: 'csharp',
    md: 'md',
    txt: 'txt',
    yaml: 'yaml',
};

program
    .name('evgen')
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    .version(require('../package.json').version, '-v, --version')
    .description('Code-generation tool for event logging')
    .requiredOption(
        '-e, --events_path <file|dir>',
        'events YAML-definitions file or directory path'
    )
    .option(
        '-c, --evgen_config_path <file>',
        'evgen generation config in YAML format',
        'evgen.yaml'
    )
    .action(async (options) => {
        try {
            const config: Config = await parseConfigFile(options.evgen_config_path);
            const events = await parseEventsFile(options.events_path, {
                keepParametersOrder: config.options?.keepParametersOrder,
            });

            const rootDir = dirname(resolve(options.evgen_config_path));
            const parsedEvents = parseEvents(events as RawEvents);

            if (config.code) {
                await Promise.all(
                    Object.values(config.code).map(async (codeConfig) => {
                        try {
                            await generateEventsCode(
                                codeConfig.language,

                                singlePlatformEvents(cloneDeep(parsedEvents), codeConfig.platform, {
                                    onlyLastVersion: codeConfig.only_last_version,
                                }),
                                {
                                    className: codeConfig.class_name,
                                    outputPath: join(rootDir, codeConfig.output_dir),
                                    templateDir: codeConfig.template_dir
                                        ? resolve(
                                              options.evgen_config_path,
                                              '..',
                                              codeConfig.template_dir
                                          )
                                        : join(
                                              DEFAULT_TEMPLATES_PATH,
                                              DEFAULT_TEMPLATES_DIRS[codeConfig.language]
                                          ),
                                    onlyLastVersion: codeConfig.only_last_version,
                                    disableSendingMeta:
                                        codeConfig.disable_sending_meta ??
                                        config.options?.disable_sending_meta,
                                }
                            );
                        } catch (e) {
                            logger.error(`Failed to generate code for ${codeConfig.platform}`, e);
                        }
                    })
                );
            }

            if (config.doc) {
                await Promise.all(
                    Object.values(config.doc).map(async (docConfig) => {
                        try {
                            await generateEventsDocs(cloneDeep(parsedEvents), {
                                outputPath: join(rootDir, docConfig.output_dir),
                                templateDir: docConfig.template_dir
                                    ? resolve(
                                          options.evgen_config_path,
                                          '..',
                                          docConfig.template_dir
                                      )
                                    : join(
                                          DEFAULT_TEMPLATES_PATH,
                                          DEFAULT_TEMPLATES_DIRS[docConfig.extension]
                                      ),
                                tag: docConfig.tag,
                            });
                        } catch (e) {
                            logger.error(
                                `Failed to generate ${docConfig.extension} documentation`,
                                e
                            );
                        }
                    })
                );
            }
        } catch (e) {
            console.error(e);
        }
    });

program.parse();
