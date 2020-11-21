"""JSON render functions."""

import json


def render(ast):
    """Render JSON."""
    return json.dumps(ast, indent=2)
