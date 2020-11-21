"""Diff renderers."""

from gendiff.formatters import json, plain, string

available_formatters = {
    'json': json.render,
    'plain': plain.render,
    'string': string.render,
}
