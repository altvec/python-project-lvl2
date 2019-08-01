# -*- coding: utf-8 -*-

"""JSON render functions."""

import json


def render_json(ast):
    """Render JSON."""
    return json.dumps(ast, indent=2)
