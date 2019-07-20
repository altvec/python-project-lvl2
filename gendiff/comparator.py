# -*- coding: utf-8 -*-


"""Comparator functions."""


def diff(file1, file2):
    """Return diff between two files."""
    diff = {}

    for key in file1:
        if key in file2:
            if file1[key] == file2[key]:
                diff['  {key}'.format(key=key)] = file1[key]
            else:
                diff['- {key}'.format(key=key)] = file1[key]
                diff['+ {key}'.format(key=key)] = file2[key]
        else:
            diff['- {key}'.format(key=key)] = file1[key]

    for key in file2:
        if key not in file1:
            diff['+ {key}'.format(key=key)] = file2[key]

    print_diff(diff)
    return diff


def print_diff(diff_data):
    """Print difference."""
    print('{')
    for item_key, item_value in diff_data.items():
        if item_value is True:
            item_value = 'true'
        if item_value is False:
            item_value = 'false'
        print('  {key}: {value}'.format(key=item_key, value=item_value))
    print('}')
