# -*- coding: utf-8 -*-

"""YAML files diff test."""

from gendiff.generator import generate_diff
from tests.expected_results import EXPECTED_SIMPLE_STRING,\
    EXPECTED_SIMPLE_PLAIN,\
    EXPECTED_SIMPLE_JSON,\
    EXPECTED_COMPLEX_STRING,\
    EXPECTED_COMPLEX_PLAIN,\
    EXPECTED_COMPLEX_JSON


def test1_simple_string():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'string')
    assert actual == EXPECTED_SIMPLE_STRING


def test2_simple_plain():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'plain')
    assert actual == EXPECTED_SIMPLE_PLAIN


def test3_simple_json():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'json')
    assert actual == EXPECTED_SIMPLE_JSON


def test4_complex_string():
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'string')
    assert actual == EXPECTED_COMPLEX_STRING


def test5_complex_plain():
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'plain')
    assert actual == EXPECTED_COMPLEX_PLAIN


def test6_complex_json():
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'json')
    assert actual == EXPECTED_COMPLEX_JSON
