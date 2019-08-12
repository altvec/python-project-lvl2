#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Gendiff script."""

from gendiff.cli import args
from gendiff.generator import generate_diff


def main():
    """Print diff between two files."""
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
