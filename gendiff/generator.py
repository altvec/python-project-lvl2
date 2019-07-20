# -*- coding: utf-8 -*-


"""Generator functions."""

import json
import yaml

from gendiff.comparator import diff


def read_file(file_name):
    """Read file and return dictionary."""
    with open(file_name, 'r', encoding='utf-8') as file_object:
        file_type = file_name.split('.')[-1]
        file_data = file_object.read()
        return parse_input(file_data, file_type)


def parse_input(file_data, file_type):
    """Parse input data into appropriate format."""
    mapping = {
        'json': lambda file_data: json.loads(file_data),
        'yaml': lambda file_data: yaml.load(file_data, Loader=yaml.SafeLoader)
    }
    return mapping[file_type](file_data)


def generate_diff(first_file, second_file, output_format=None):
    """Generate diff."""
    diff(read_file(first_file), read_file(second_file))
