# -*- coding: utf-8 -*-

"""Renderer functions."""

from gendiff.renderers.render_json import render_json
from gendiff.renderers.render_plain import render_plain
from gendiff.renderers.render_string import render_string


def render(file_format, ast):
    """Render data into appropriate format."""
    mapping = {
        'json': render_json,
        'plain': render_plain,
        'string': render_string,
    }
    if file_format not in mapping:
        return 'Unsupported formatter'
    return mapping[file_format](ast)
