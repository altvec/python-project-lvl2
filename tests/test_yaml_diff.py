# -*- coding: utf-8 -*-

"""YAML files diff test."""

from gendiff.generator import generate_diff
import tests.expected as expected


def test1_simple_string():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'string')
    assert actual == expected.SIMPLE_STRING


def test2_simple_plain():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'plain')
    assert actual == expected.SIMPLE_PLAIN


def test3_simple_json():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'json')
    assert actual == expected.SIMPLE_JSON


def test4_complex_string():
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'string')
    assert actual == expected.COMPLEX_STRING


def test5_complex_plain():
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'plain')
    assert actual == expected.COMPLEX_PLAIN


def test6_complex_json():
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'json')
    assert actual == expected.COMPLEX_JSON
