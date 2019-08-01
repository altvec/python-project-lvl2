# -*- coding: utf-8 -*-

"""Generator functions."""

import json

import yaml

from gendiff.ast_builder import build_ast
from gendiff.renderers.render import render


def read_file(file_name):
    """Read file and return dictionary."""
    with open(file_name, 'r', encoding='utf-8') as file_object:
        file_type = file_name.split('.')[-1]
        file_data = file_object.read()
        return parser(file_data, file_type)


def parser(file_data, file_type):
    """Parse input data into appropriate format."""
    mapping = {
        'json': json.loads,
        'yaml': lambda file_data: yaml.load(file_data, Loader=yaml.SafeLoader),
    }
    return mapping[file_type](file_data)


def generate_diff(first_file, second_file, file_format):
    """Generate diff."""
    if not file_format:
        file_format = 'plain'
    first, second = read_file(first_file), read_file(second_file)
    ast = build_ast(first, second)
    diff = render(file_format, ast)
    return diff
