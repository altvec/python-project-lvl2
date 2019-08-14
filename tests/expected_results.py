# -*- coding: utf-8 -*-

"""Expected results constants."""

SIMPLE_STRING = '''{
    host: hexlet.io
  - proxy: 123.234.53.22
  + timeout: 20
  - timeout: 50
  + verbose: true
}'''

SIMPLE_PLAIN = '''Property 'proxy' was removed
Property 'timeout' was changed. From '50' to '20'
Property 'verbose' was added with value: 'true\''''

SIMPLE_JSON = '''{
  "host": {
    "type": "unchanged",
    "key": "host",
    "value": "hexlet.io"
  },
  "proxy": {
    "type": "removed",
    "key": "proxy",
    "value": "123.234.53.22"
  },
  "timeout": {
    "type": "changed",
    "key": "timeout",
    "old_value": 50,
    "new_value": 20
  },
  "verbose": {
    "type": "added",
    "key": "verbose",
    "value": "true"
  }
}'''

COMPLEX_STRING = '''{
    common: {
        setting1: Value 1
      - setting2: 200
        setting3: true
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
      - setting6: {
            key: value
        }
    }
    group1: {
      + baz: bars
      - baz: bas
        foo: bar
    }
  - group2: {
        abc: 12345
    }
  + group3: {
        fee: 100500
    }
}'''

COMPLEX_PLAIN = '''Property 'common.setting2' was removed
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: 'complex value'
Property 'common.setting6' was removed
Property 'group1.baz' was changed. From 'bas' to 'bars'
Property 'group2' was removed
Property 'group3' was added with value: 'complex value\''''

COMPLEX_JSON = '''{
  "common": {
    "type": "parent",
    "name": "common",
    "child": {
      "setting1": {
        "type": "unchanged",
        "key": "setting1",
        "value": "Value 1"
      },
      "setting2": {
        "type": "removed",
        "key": "setting2",
        "value": "200"
      },
      "setting3": {
        "type": "unchanged",
        "key": "setting3",
        "value": "true"
      },
      "setting4": {
        "type": "added",
        "key": "setting4",
        "value": "blah blah"
      },
      "setting5": {
        "type": "added",
        "key": "setting5",
        "value": {
          "key5": "value5"
        }
      },
      "setting6": {
        "type": "removed",
        "key": "setting6",
        "value": {
          "key": "value"
        }
      }
    }
  },
  "group1": {
    "type": "parent",
    "name": "group1",
    "child": {
      "baz": {
        "type": "changed",
        "key": "baz",
        "old_value": "bas",
        "new_value": "bars"
      },
      "foo": {
        "type": "unchanged",
        "key": "foo",
        "value": "bar"
      }
    }
  },
  "group2": {
    "type": "removed",
    "key": "group2",
    "value": {
      "abc": "12345"
    }
  },
  "group3": {
    "type": "added",
    "key": "group3",
    "value": {
      "fee": "100500"
    }
  }
}'''
