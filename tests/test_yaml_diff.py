# -*- coding: utf-8 -*-

"""YAML files diff test."""


import pytest

from gendiff.generator import generate_diff


def test1_simple_string():
    expected = (
        '{\n'
        '    host: hexlet.io\n'
        '  - proxy: 123.234.53.22\n'
        '  + timeout: 20\n'
        '  - timeout: 50\n'
        '  + verbose: true\n'
        '}'
    )
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'string')
    assert actual == expected


def test2_simple_plain():
    # expected = (
    #     "Property 'proxy' was removed\n"
    #     "Property 'timeout' was changed. From '50' to '20'\n"
    #     "Property 'verbose' was added with value: 'true'"
    # )
    # actual = generate_diff('./tests/fixtures/simple_before.yaml',
    #                        './tests/fixtures/simple_after.yaml',
    #                        'plain')
    # assert actual == expected
    pass


def test3_simple_json():
    expected = (
        '{\n'
        '  "host": {\n'
        '    "type": "unchanged",\n'
        '    "key": "host",\n'
        '    "value": "hexlet.io"\n'
        '  },\n'
        '  "proxy": {\n'
        '    "type": "removed",\n'
        '    "key": "proxy",\n'
        '    "value": "123.234.53.22"\n'
        '  },\n'
        '  "timeout": {\n'
        '    "type": "changed",\n'
        '    "key": "timeout",\n'
        '    "old_value": 50,\n'
        '    "new_value": 20\n'
        '  },\n'
        '  "verbose": {\n'
        '    "type": "added",\n'
        '    "key": "verbose",\n'
        '    "value": true\n'
        '  }\n'
        '}'
    )
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'json')
    assert actual == expected


def test4_complex_string():
    expected = (
        '{\n'
        '    common: {\n'
        '        setting1: Value 1\n'
        '      - setting2: 200\n'
        '        setting3: true\n'
        '      + setting4: blah blah\n'
        '      + setting5: {\n'
        '            key5: value5\n'
        '        }\n'
        '      - setting6: {\n'
        '            key: value\n'
        '        }\n'
        '    }\n'
        '    group1: {\n'
        '      + baz: bars\n'
        '      - baz: bas\n'
        '        foo: bar\n'
        '    }\n'
        '  - group2: {\n'
        '        abc: 12345\n'
        '    }\n'
        '  + group3: {\n'
        '        fee: 100500\n'
        '    }\n'
        '}'
    )
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'string')
    assert actual == expected


def test5_complex_plain():
    # expected = (
    #     "Property 'common.setting2' was removed\n"
    #     "Property 'common.setting4' was added with value: 'blah blah'\n"
    #     "Property 'common.setting5' was added with value: 'complex value'\n"
    #     "Property 'common.setting6' was removed\n"
    #     "Property 'group1.baz' was changed. From 'bas' to 'bars'\n"
    #     "Property 'group2' was removed\n"
    #     "Property 'group3' was added with value: 'complex value'"
    # )
    # actual = generate_diff('./tests/fixtures/complex_before.yaml',
    #                        './tests/fixtures/complex_after.yaml',
    #                        'plain')
    # assert actual == expected
    pass


def test6_complex_json():
    pass
