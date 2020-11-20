# Generate diff

[![Github Actions Status](https://github.com/altvec/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/altvec/python-project-lvl2/actions)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Maintainability](https://api.codeclimate.com/v1/badges/91dea468d18ac43f14a4/maintainability)](https://codeclimate.com/github/altvec/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/91dea468d18ac43f14a4/test_coverage)](https://codeclimate.com/github/altvec/python-project-lvl2/test_coverage)

CLI utility for finding differences between configuration files.

## Installation

```bash
pip install --user --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ altvec-gendiff
```

[![asciicast](https://asciinema.org/a/zWdiPRzNsa0GnjYPVz4x6mW8E.svg)](https://asciinema.org/a/zWdiPRzNsa0GnjYPVz4x6mW8E)

## Comparing flat JSON files

```bash
gendiff simple_before.json simple_after.json
```

If `format` option is omitted, output will be in `string` by default.

[![asciicast](https://asciinema.org/a/9yjT0m0EH5YLqdUid1oSkNxgw.svg)](https://asciinema.org/a/9yjT0m0EH5YLqdUid1oSkNxgw)

## Comparing files with nested structures

```bash
gendiff -f string complex_before.json complex_after.json
```

[![asciicast](https://asciinema.org/a/qIsw8Ta6Ac950Lg3c8fHxZp2O.svg)](https://asciinema.org/a/qIsw8Ta6Ac950Lg3c8fHxZp2O)

## Plain text format for output

```bash
gendiff -f plain before.json after.json
```

[![asciicast](https://asciinema.org/a/aXK48JaC8f0mr9iMPA73sA6Bg.svg)](https://asciinema.org/a/aXK48JaC8f0mr9iMPA73sA6Bg)
