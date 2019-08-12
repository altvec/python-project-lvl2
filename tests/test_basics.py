# -*- coding: utf-8 -*-

"""Basic tests."""

from gendiff.generator import generate_diff


def test_usupported_formatter():
    expected = 'Unsupported formatter'
    actual = generate_diff('./tests/fixtures/complex_before.json',
                           './tests/fixtures/complex_after.json',
                           'deadbeef')
    assert actual == expected
