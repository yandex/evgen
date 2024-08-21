# Code generation for event logging

[![npm version](https://badger.yandex-team.ru/npm/@kinopoisk-int/evgen/version.svg)](https://npm.yandex-team.ru/-/ui/package/@kinopoisk-int/evgen) [![OKO: distribution health](https://badger.yandex-team.ru/oko/pkg/@kinopoisk-int/evgen/health.svg)](https://oko.yandex-team.ru/packages/%40kinopoisk-int%2Fevgen) [![oko health](https://oko.yandex-team.ru/badges/repo.svg?repoName=kinopoisk%2Ffrontend%2Fpackages%2Fevgen&vcs=arcadia)](https://oko.yandex-team.ru/projects/kinopoisk%2Ffrontend%2Fpackages%2Fevgen) [![oko health](https://oko.yandex-team.ru/badges/repoSecurity.svg?repoName=kinopoisk/frontend/packages/evgen&vcs=arcadia)](https://oko.yandex-team.ru/projects/kinopoisk%2Ffrontend%2Fpackages%2Fevgen) [![owners](https://badger.yandex-team.ru/custom/[ABC]/[Kinopoisk%20Frontend%20Infrastructure][green]/badge.svg)](https://abc.yandex-team.ru/services/kpott_infrafront/)

EvGen: Event Generator.  Useful tools for making contracts between analysts and developers.

Supported languages

   - swift
   - java
   - kotlin
   - type_script

## Table of Contents

-   [Install](#install)
-   [Usage](#usage)

## Install

```bash
npm install -g evgen
```

## Usage

0. Create a folder with:
    * events.yaml -- File with event specifications
    * evgen.yaml -- Evgen config file
1. ```evgen --events_path events.yaml --evgen_config_path evgen.yaml``` or ```evgen -e events.yaml -c evgen.yaml```
2. Without installing: ```npx evgen -e events.yaml -c evgen.yaml```

Examples of evgen.yaml can be found in tutorial/

Structure of evgen.yaml

```
code:
  configName1:
    platform: 'Android'
    output_dir: 'android'
    language: 'java'
    class_name: 'EvgenAppAnalytics'

  ...

doc:
  Markdown:
    extension: 'md'
    output_dir: 'md_doc'
  Txt:
    extension: 'txt'
    output_dir: 'txt_doc'
```

### Templates
To customize generated files you can create your own generation templates and specify it in evgen.yaml:
```
code:
  configName1:
    platform: 'Android'
    output_dir: 'android'
    language: 'java'
    class_name: 'EvgenAppAnalytics'
    template_dir: relative/path/to/your/java-templates

  ...

doc:
  Markdown:
    extension: 'md'
    output_dir: 'md_doc'
    template_dir: relative/path/to/your/md-templates
  Txt:
    extension: 'txt'
    output_dir: 'txt_doc'
    template_dir: relative/path/to/your/txt-templates
```

You can see default templates in `src/templates` directory. It is [Handlebars](https://handlebarsjs.com/) format extended by additional [handlebars-helpers](https://github.com/helpers/handlebars-helpers) and local helpers from `src/helpers` directory.
