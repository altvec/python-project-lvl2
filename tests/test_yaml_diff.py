# -*- conding: utf-8 -*-

"""JSON files diff test."""

import unittest
import yaml

from gendiff.comparator import diff


class TestJson(unittest.TestCase):
    """Test the YAML diff."""

    def test_file1_file2_diff(self):
        data1 = yaml.load("""
            timeout: 20
            verbose: true
            host: hexlet.io
        """, Loader=yaml.SafeLoader)
        data2 = yaml.load("""
            host: hexlet.io
            timeout: 50
            proxy: 123.234.53.22
        """, Loader=yaml.SafeLoader)
        print(data1)
        print(data2)
        result = diff(data1, data2)
        expect = {
            '  host': 'hexlet.io',
            '+ timeout': '50',
            '- timeout': '20',
            '+ proxy': '123.234.53.22',
            '- verbose': 'true'
        }
        print(sorted(result))
        print(sorted(expect))
        self.assertEqual(sorted(result), sorted(expect))
