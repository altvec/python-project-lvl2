# -*- coding: utf-8 -*-

"""Plain render functions."""

from gendiff.constants import (
    ADDED,
    CHANGED,
    COMPLEX,
    NESTED,
    REMOVED,
    UNCHANGED,
)


def render_plain(ast, parent=''):
    """Render plain text."""
    if not isinstance(ast, dict):
        return str(ast)
    result_array, entry = [], ''
    for node_key, node_value in ast.items():
        prop = _get_property(parent, node_key)
        node_type = node_value.get('type')
        if node_type == ADDED:
            entry = "Property '{prop}' was added with value: '{value}'".format(
                prop=prop,
                value=_get_value(node_value),
            )
        elif node_type == REMOVED:
            entry = "Property '{prop}' was removed".format(prop=prop)
        elif node_type == NESTED:
            entry = render_plain(node_value.get('value'), prop)
        elif node_type == CHANGED:
            template = "Property '{prop}' was changed. From '{old}' to '{new}'"
            entry = template.format(
                prop=prop,
                old=node_value.get('old_value'),
                new=node_value.get('new_value'),
            )
        elif node_type == UNCHANGED:
            continue
        result_array.append(entry)
    return '\n'.join(result_array).strip()


def _get_value(node):
    node_value = node.get('value')
    if isinstance(node_value, dict):
        return COMPLEX
    return str(node_value)


def _get_property(parent, prop_name):
    if not parent:
        return prop_name
    return '{parent}.{prop}'.format(parent=parent, prop=prop_name)
