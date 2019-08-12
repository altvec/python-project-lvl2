# -*- coding: utf-8 -*-

"""AST building functions."""

from gendiff.constants import ADDED, CHANGED, REMOVED, UNCHANGED


def build_ast(before, after):
    """Build AST."""
    keys = list(before.keys() | after.keys())
    ast = {key: gen_node(key, before, after) for key in sorted(keys)}
    return ast


def gen_node(key, before, after):
    """Generate tree nodes."""
    if key not in before:
        node = {
            'type': ADDED,
            'key': key,
            'value': _get_value_type(after[key]),
        }
    elif key not in after:
        node = {
            'type': REMOVED,
            'key': key,
            'value': _get_value_type(before[key]),
        }
    elif isinstance(before[key], dict) and isinstance(after[key], dict):
        node = {
            'type': 'parent',
            'name': key,
            'child': build_ast(before[key], after[key]),
        }
    elif before[key] == after[key]:
        node = {
            'type': UNCHANGED,
            'key': key,
            'value': _get_value_type(before[key]),
        }
    elif before[key] != after[key]:
        node = {
            'type': CHANGED,
            'key': key,
            'old_value': _get_value_type(before[key]),
            'new_value': _get_value_type(after[key]),
        }
    return node


def _get_value_type(elem_value):
    if elem_value is True:
        return 'true'
    if elem_value is False:
        return 'false'
    return elem_value
