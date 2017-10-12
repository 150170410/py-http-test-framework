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
        value = 'cookie_value'
        httpbin_url = 'https://httpbin.org/cookies'

        http_session = HttpSession()

        http_session.update_cookies({
            'test_cookie': value
        })
        response = http_session.get(httpbin_url).json()
        self.assertEqual(response['cookies']['test_cookie'], value)

        http_session.update_cookies({
            'test_cookie': value + '+1',
            'test_cookie2': value
        })
        response = http_session.get(httpbin_url).json()
        self.assertEqual(response['cookies']['test_cookie'], value + '+1')
        self.assertEqual(response['cookies']['test_cookie2'], value)

    def test_update_headers(self):
        """
        test_update_headers
        :return:
        """
        value = 'header_value'
        httpbin_url = 'https://httpbin.org/headers'

        http_session = HttpSession()

        http_session.update_headers({
            'test_header': value
        })
        response = http_session.get(httpbin_url).json()
        self.assertEqual(response['headers']['Test-Header'], value)

        http_session.update_headers({
            'test_header': value + '+1',
            'test_header2': value
        })
        response = http_session.get(httpbin_url).json()
        self.assertEqual(response['headers']['Test-Header'], value + '+1')
        self.assertEqual(response['headers']['Test-Header2'], value)
