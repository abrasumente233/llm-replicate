# llm-replicate

[![PyPI](https://img.shields.io/pypi/v/llm-replicate.svg)](https://pypi.org/project/llm-replicate/)
[![Changelog](https://img.shields.io/github/v/release/abrasumente233/llm-replicate?include_prereleases&label=changelog)](https://github.com/abrasumente233/llm-replicate/releases)
[![Tests](https://github.com/abrasumente233/llm-replicate/actions/workflows/test.yml/badge.svg)](https://github.com/abrasumente233/llm-replicate/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/abrasumente233/llm-replicate/blob/main/LICENSE)

Access [replicate.com](https://replicate.com/) models via API

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-replicate
```
## Usage

Obtain a [Replicate API key](https://replicate.com/account/api-tokens) and save it like this:

```bash
llm keys set replicate
# <Paste key here>
```
Run `llm models` to get a list of models.

Run prompts like this:
```bash
llm -m replicate-chat 'five great names for a pet ocelot'
llm -m replicate-reasoner 'solve \\int \\frac{\\ln(x)\\arctan(x)}{x^2+1} dx'
llm -m replicate-coder 'how to reverse a linked list in python'
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-replicate
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
