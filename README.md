# Code generation for event logging

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
