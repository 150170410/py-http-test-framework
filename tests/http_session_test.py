#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from py_http_api_test.http_session import HttpSession


class HttpSessionTest(unittest.TestCase):
    """
    测试http_session模块
    """
    def test_update_cookies(self):
        """
        test_update_cookies
        :return:
        """
        cookie_value = 'cookie_value'
        httpbin_url = 'https://httpbin.org/cookies'

        http_session = HttpSession()

        http_session.update_cookies({
            'cookie1': cookie_value
        })
        response = http_session.get(httpbin_url).json()
        self.assertEqual(response['cookies']['cookie1'], cookie_value)

        http_session.update_cookies({
            'cookie2': cookie_value
        })
        response = http_session.get(httpbin_url).json()
        self.assertEqual(response['cookies']['cookie1'], cookie_value)
        self.assertEqual(response['cookies']['cookie2'], cookie_value)

    def test_update_headers(self):
        """
        test_update_headers
        :return:
        """
        header_value = 'header_value'
        httpbin_url = 'https://httpbin.org/headers'

        http_session = HttpSession()

        http_session.update_headers({
            'test_header': header_value
        })
        response = http_session.get(httpbin_url).json()
        self.assertEqual(response['headers']['Test-Header'], header_value)
