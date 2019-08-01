# -*- coding: utf-8 -*-

"""Plain render functions."""


def render_plain(ast):
    """Render plain text."""
    changes = _get_changes(ast)
    return '\n'.join(changes)


def _get_changes(ast, parent=None, res=[]):
    for element in ast.values():
        if element['type'] == 'parent':
            _get_changes(element['child'], element['name'])
        if element['type'] == 'removed':
            prop_name = _get_property(element, parent)
            res.append("Property '{prop}' was removed".format(
                prop=prop_name,
            ))
        if element['type'] == 'added':
            prop_name = _get_property(element, parent)
            prop_value = _get_value(element['value'])
            res.append(
                "Property '{prop}' was added with value: '{value}'".format(
                    prop=prop_name,
                    value=prop_value,
                ))
        if element['type'] == 'changed':
            prop_name = _get_property(element, parent)
            new_value = _get_value(element['new_value'])
            old_value = _get_value(element['old_value'])
            res.append(
                "Property '{prop}' was changed. From '{old}' to '{new}'".format(
                    prop=prop_name,
                    old=old_value,
                    new=new_value,
                ))
    return res


def _get_value(prop_value):
    if prop_value is True:
        return 'true'
    if prop_value is False:
        return 'false'
    if isinstance(prop_value, dict):
        return 'complex value'
    return prop_value


def _get_property(element, parent):
    name = element['key']
    if parent is None:
        return '{name}'.format(name=name)
    return '{parent}.{name}'.format(parent=parent, name=name)
