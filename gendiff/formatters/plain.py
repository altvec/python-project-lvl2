"""Plain render functions."""

from gendiff.constants import (
    ADDED,
    CHANGED,
    COMPLEX,
    NESTED,
    REMOVED,
    UNCHANGED,
)

ADDED_TMPL = "Property '{0}' was added with value: '{1}'"
REMOVED_TMPL = "Property '{0}' was removed"
CHANGED_TMPL = "Property '{0}' was changed. From '{1}' to '{2}'"


def render(ast, parent=''):
    """Render plain text."""
    if not isinstance(ast, dict):
        return str(ast)

    result_array = []

    for node_key, node_value in ast.items():
        prop = get_property(parent, node_key)
        node_type = node_value.get('type')

        if node_type == ADDED:
            entry = ADDED_TMPL.format(prop, get_value(node_value))
        elif node_type == REMOVED:
            entry = REMOVED_TMPL.format(prop)

        if node_type == NESTED:
            entry = render(node_value.get('value'), prop)
        elif node_type == CHANGED:
            entry = CHANGED_TMPL.format(
                prop,
                node_value.get('old_value'),
                node_value.get('new_value'),
            )
        elif node_type == UNCHANGED:
            continue

        result_array.append(entry)
    return '\n'.join(result_array)


def get_value(node):
    """Return node value."""
    node_value = node.get('value')
    if isinstance(node_value, dict):
        return COMPLEX
    return str(node_value)


def get_property(parent, prop_name):
    """Return property value."""
    if not parent:
        return prop_name
    return '{parent}.{prop}'.format(parent=parent, prop=prop_name)
