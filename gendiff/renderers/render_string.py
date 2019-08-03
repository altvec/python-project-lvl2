# -*- coding: utf-8 -*-

"""JSON-like string render functions."""


def render_string(ast):
    """Render pseudo JSON as string."""
    changes = _get_changes(ast)
    return '{{\n{changes}\n}}'.format(changes=changes)


def _get_changes(ast, depth=1):
    indent = '  ' * depth
    res = []
    for element in ast.values():
        if element['type'] == 'parent':
            res.append('  {indent}{name}: {{\n{childs}\n  {indent}}}'.format(
                indent=indent,
                name=element['name'],
                childs=_get_changes(element['child'], depth + 2),
            ))
        if element['type'] == 'added':
            res.append('{indent}+ {name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['value'], depth),
            ))
        if element['type'] == 'removed':
            res.append('{indent}- {name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['value'], depth),
            ))
        if element['type'] == 'unchanged':
            res.append('  {indent}{name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['value'], depth),
            ))
        if element['type'] == 'changed':
            res.append('{indent}+ {name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['new_value'], depth),
            ))
            res.append('{indent}- {name}: {value}'.format(
                indent=indent,
                name=element['key'],
                value=_get_value(element['old_value'], depth),
            ))
    return '\n'.join(res)


def _get_value(element, depth):
    if element is True:
        return 'true'
    if element is False:
        return 'false'
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
