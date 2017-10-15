#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest

from py_http_api_test.jmespath_custom import search


class JmespathCustomTest(unittest.TestCase):
    """
    测试jmespath_custom模块
    """
    def test_search(self):
        """
        test_search
        :return:
        """
        json_data = {
            'key': 'value'
        }

        self.assertEqual(search('key', json_data), 'value')

    def test_str_to_unicode(self):
        """
        test_str_to_unicode
        :return:
        """
        json_str = """
        {
        "machines": [
                {"name": "a", "state": "开始"},
                {"name": "b", "state": "结束"},
                {"name": "c", "state": "开始"}
            ]
        }
        """
        json_data = json.loads(json_str)

        self.assertEqual(search("machines[?state==str_to_unicode('结束')].name", json_data), ['b'])
