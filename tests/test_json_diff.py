# -*- conding: utf-8 -*-

"""JSON files diff test."""

import unittest
import json

from gendiff.comparator import diff


class TestJson(unittest.TestCase):
    """Test the JSON diff."""

    def test_file1_file2_diff(self):
        data1 = {
            'timeout': '20',
            'verbose': 'true',
            'host': 'hexlet.io',
        }
        data2 = {
            'host': 'hexlet.io',
            'timeout': '50',
            'proxy': '123.234.53.22',
        }
        result = diff(data1, data2)
        expect = {
            '  host': 'hexlet.io',
            '- timeout': '50',
            '+ timeout': '20',
            '- proxy': '123.234.53.22',
            '+ verbose': 'true'
        }
        self.assertEqual(sorted(json.dumps(result)), sorted(json.dumps(expect)))
