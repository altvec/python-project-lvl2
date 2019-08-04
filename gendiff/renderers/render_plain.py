# -*- coding: utf-8 -*-

"""Plain render functions."""


def render_plain(ast, parent=None):
    """Render plain text."""
    changes = [
        _get_changes(element, parent) for element in ast.values()
    ]
    return '\n'.join(filter(lambda element: element is not None, changes))


def _get_changes(element, parent=None):
    if element['type'] == 'parent':
        return render_plain(element['child'], element['name'])
    if element['type'] == 'removed':
        return "Property '{prop}' was removed".format(
            prop=_get_property(element, parent),
        )
    if element['type'] == 'added':
        return "Property '{prop}' was added with value: '{value}'".format(
            prop=_get_property(element, parent),
            value=_get_value(element['value']),
        )
    if element['type'] == 'changed':
        return "Property '{prop}' was changed. From '{old}' to '{new}'".format(
            prop=_get_property(element, parent),
            old=_get_value(element['old_value']),
            new=_get_value(element['new_value']),
        )


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
