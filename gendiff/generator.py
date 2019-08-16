# -*- coding: utf-8 -*-

"""Generator functions."""

import os

from gendiff.ast_builder import build_ast
from gendiff.input_parser import parser
from gendiff.renderers.render import render


def read_file(file_name):
    """Read file and return dictionary."""
    with open(file_name, 'r', encoding='utf-8') as file_object:
        file_type = os.path.splitext(file_name)[-1]
        file_data = file_object.read()
        return parser(file_data, file_type)


def generate_diff(first_file, second_file, output_format):
    """Generate diff."""
    if not output_format:
        output_format = 'plain'
    first, second = read_file(first_file), read_file(second_file)
    ast = build_ast(first, second)
    diff = render(output_format, ast)
    return diff
