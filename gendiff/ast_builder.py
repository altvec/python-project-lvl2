# -*- coding: utf-8 -*-

"""AST building functions."""


from gendiff.constants import ADDED, CHANGED, REMOVED, UNCHANGED


def build_ast(before, after):
    """Build AST."""
    keys = set(before.keys()) | set(after.keys())
    ast = {key: gen_node(key, before, after) for key in sorted(keys)}
    return ast


def gen_node(key, before, after):
    """Generate tree nodes."""
    if key not in before:
        node = {
            'type': ADDED,
            'key': key,
            'value': after[key],
        }
    elif key not in after:
        node = {
            'type': REMOVED,
            'key': key,
            'value': before[key],
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
            'value': before[key],
        }
    elif before[key] != after[key]:
        node = {
            'type': CHANGED,
            'key': key,
            'old_value': before[key],
            'new_value': after[key],
        }
    return node
