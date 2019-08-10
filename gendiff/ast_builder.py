# -*- coding: utf-8 -*-

"""AST building functions."""


def build_ast(file1, file2):
    """Build AST."""
    keys = set(file1.keys()) | set(file2.keys())
    ast = {key: gen_nodes(key, file1, file2) for key in sorted(keys)}
    return ast


def gen_nodes(key, file1, file2):
    """Generate tree nodes."""
    if key not in file1:
        return {
            'type': 'added',
            'key': key,
            'value': file2[key],
        }
    if key not in file2:
        return {
            'type': 'removed',
            'key': key,
            'value': file1[key],
        }
    if isinstance(file1[key], dict) and isinstance(file2[key], dict):
        return {
            'type': 'parent',
            'name': key,
            'child': build_ast(file1[key], file2[key]),
        }
    if file1[key] == file2[key]:
        return {
            'type': 'unchanged',
            'key': key,
            'value': file1[key],
        }
    if file1[key] != file2[key]:
        return {
            'type': 'changed',
            'key': key,
            'old_value': file1[key],
            'new_value': file2[key],
        }
