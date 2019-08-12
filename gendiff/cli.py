# -*- coding: utf-8 -*-

"""Command-line options parser."""

import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', metavar='first_file', type=str)
parser.add_argument('second_file', metavar='second_file', type=str)
parser.add_argument(
    '-f',
    '--format',
    action='store',
    help='set format of output',
)

args = parser.parse_args()
