# Code generation for event logging

EvGen: Event Generator.  Useful tools for making contracts between analysts and developers.

Supported languages

   - swift
   - java
   - kotlin
   - type_script
   - java_script
   - с_sharp

## Prerequisites

- [python >= 3.8](https://www.python.org/downloads/)
- [poetry](https://python-poetry.org/docs/#installation)

## Installation

```sh
poetry install
```

You can now use it from the project package

> Scripts to run are defined in `pyproject.toml`

```sh
poetry run run_evgen # and additional arguments
```

If you want to install it globally, you have to build a project

```sh
poetry build --format wheel
pip install ./dist/evgen-{PACKAGE_VERSION}-py3-none-any.whl
```

## Run generation

0. Create a folder with:
    * events.yaml -- File with event specifications
    * evgen.yaml -- Evgen config file
1. ```run_evgen.py --events_path events.yaml --evgen_config_path evgen.yaml```
Examples of evgen.yaml can be found in tutorial/

Structure of evgen.yaml

```code:
  $SubconfigName1:
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

## Check generated file consistency

We suggest checking the consistency of the yaml and generated files. To see if generated files were changed manually:
```check_evgen_result.py --events_yaml_path events.yaml --evgen_config_path evgen.yaml```
