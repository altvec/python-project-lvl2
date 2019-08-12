# -*- coding: utf-8 -*-

"""JSON-like string render functions."""

from gendiff.constants import ADDED, CHANGED, REMOVED, UNCHANGED


def render_string(ast):
    """Render pseudo JSON as string."""
    changes = _get_changes(ast)
    return '{{\n{changes}\n}}'.format(changes=changes)


def _get_changes(ast, depth=1):
    indent = '  ' * depth
    res = []
    for element in ast.values():
        element_type = element['type']
        if element_type == 'parent':
            change = '  {indent}{name}: {{\n{childs}\n  {indent}}}'.format(
                indent=indent,
                name=element['name'],
                childs=_get_changes(element['child'], depth + 2),
            )
        if element_type == ADDED:
            change = '{indent}+ {name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['value'], depth),
            )
        if element_type == REMOVED:
            change = '{indent}- {name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['value'], depth),
            )
        if element_type == UNCHANGED:
            change = '  {indent}{name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['value'], depth),
            )
        if element_type == CHANGED:
            change = '{indent}+ {name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['new_value'], depth),
            )
            change += '\n{indent}- {name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['old_value'], depth),
            )
        res.append(change)
    return '\n'.join(res)


def _get_value(element, depth):
    if isinstance(element, dict):
        return _render_array(element, depth)
    return element


def _render_array(elements, depth):
    indent = '  ' * depth
    res = []
    for prop_name, prop_value in elements.items():
        res.append('{{\n      {indent}{name}: {value}\n  {indent}}}'.format(
            indent=indent,
            name=prop_name,
            value=prop_value,
        ))
    return '\n'.join(res)
