# -*- coding: utf-8 -*-

"""JSON-like string render functions."""

from gendiff.constants import (
    ADDED,
    CHANGED,
    INDENT,
    NESTED,
    REMOVED,
    UNCHANGED,
)


def render_string(ast, depth=1):
    """Render pseudo JSON as string."""
    diff = []
    indent = INDENT * depth
    for node_key, node_value in ast.items():
        item_type = node_value.get('type')
        item_value = node_value.get('value')
        if item_type == NESTED:
            diff.append('{indent}{state} {key}: {{'.format(
                indent=indent,
                state=UNCHANGED,
                key=node_key,
            ))
            diff.append(render_string(item_value, depth + 2))
            diff.append('{indent}}}'.format(indent=indent + INDENT))
        elif item_type == CHANGED:
            diff.append('{indent}{state} {key}: {value}'.format(
                indent=indent,
                state=ADDED,
                key=node_key,
                value=node_value.get('new_value'),
            ))
            diff.append('{indent}{state} {key}: {value}'.format(
                indent=indent,
                state=REMOVED,
                key=node_key,
                value=node_value.get('old_value'),
            ))
        else:
            diff.append('{indent}{state} {key}: {value}'.format(
                indent=indent,
                state=item_type,
                key=node_key,
                value=_get_value(item_value, depth),
            ))
    if depth == 1:
        diff = ['{'] + diff + ['}']
    return '\n'.join(diff)


def _get_value(element, depth=1):
    if isinstance(element, dict):
        return _render_array(element, depth)
    return element


def _render_array(elements, depth):
    res = []
    res.append('{')
    for prop_name, prop_value in elements.items():
        res.append('{indent}{name}: {value}'.format(
            indent=INDENT * (depth + 3),
            name=prop_name,
            value=prop_value,
        ))
        res.append('{indent}}}'.format(
            indent=INDENT * (depth + 1),
        ))
    return '\n'.join(res)
