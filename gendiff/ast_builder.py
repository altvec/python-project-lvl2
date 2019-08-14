# -*- coding: utf-8 -*-

"""AST building functions."""

from gendiff.constants import ADDED, CHANGED, REMOVED, PARENT, UNCHANGED


def build_ast(before, after):
    """Build AST."""
    keys = list(before.keys() | after.keys())
    ast = {key: gen_node(key, before, after) for key in sorted(keys)}
    return ast


def gen_node(key, before, after):
    """Generate tree nodes."""
    after_value = after.get(key)
    before_value = before.get(key)
    if before_value is None:
        node = {
            'type': ADDED,
            'key': key,
            'value': _get_value_type(after_value),
        }
    elif after_value is None:
        node = {
            'type': REMOVED,
            'key': key,
            'value': _get_value_type(before_value),
        }
    elif isinstance(before_value, dict) and isinstance(after_value, dict):
        node = {
            'type': PARENT,
            'name': key,
            'child': build_ast(before_value, after_value),
        }
    elif before_value == after_value:
        node = {
            'type': UNCHANGED,
            'key': key,
            'value': _get_value_type(before_value),
        }
    elif before_value != after_value:
        node = {
            'type': CHANGED,
            'key': key,
            'old_value': _get_value_type(before_value),
            'new_value': _get_value_type(after_value),
        }
    return node


def _get_value_type(elem_value):
    if elem_value is True:
        return 'true'
    if elem_value is False:
        return 'false'
    return elem_value
