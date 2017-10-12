#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from Crypto import Random
from Crypto.Cipher import AES

from py_http_api_test import tools


class ToolsTest(unittest.TestCase):
    """
    tools模块单测
    """
    def test_random_number(self):
        """
        test_random_number
        :return:
        """
        num = tools.random_number(0, 100)
        self.assertGreaterEqual(num, 0)
        self.assertLessEqual(num, 100)

    def test_sort_by_value(self):
        """
        test_sort_by_value
        :return:
        """
        dict_data = {
            'b': 2,
            'a': 1,
            'c': 3,
        }

        self.assertEqual(tools.sort_by_value(dict_data), [('a', 1), ('b', 2), ('c', 3)])

    def test_get_random_shuffle_list(self):
        """
        test_get_random_shuffle_list
        :return:
        """
        list_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.assertNotEqual(tools.get_random_shuffle_list(list_data), list_data)
        self.assertEqual(sorted(tools.get_random_shuffle_list(list_data)), list_data)

    def test_md5(self):
        """
        test_md5
        :return:
        """
        s = '0123456789'
        cn_s = '中文字符串'

        self.assertEqual(tools.md5(s), '781e5e245d69b566979b86e28d23f2c7')
        self.assertEqual(tools.md5(cn_s), '353c198568f0cd08eb215d21f45938a3')

    def test_current_time(self):
        """
        test_current_time
        :return:
        """
        self.assertGreaterEqual(tools.current_time(), 150000000)

    def test_current_time_millis(self):
        """
        test_current_time_millis
        :return:
        """
        self.assertGreaterEqual(tools.current_time_millis(), 150000000000)

    def test_base64_urlsafe_decode(self):
        """
        test_base64_urlsafe_decode
        :return:
        """
        # 正常编码
        self.assertEqual(tools.base64_urlsafe_decode('QmFzZTY05Yqg5a+G6Kej5a+G'), 'Base64加密解密')
        # url safe编码
        self.assertEqual(tools.base64_urlsafe_decode('QmFzZTY05Yqg5a-G6Kej5a-G'), 'Base64加密解密')
        # 需补充'='的场景
        self.assertEqual(tools.base64_urlsafe_decode('MA'), '0')

    def test_encrypter(self):
        """
        test_encrypter
        :return:
        """
        key = '0123456701234567'
        iv = Random.new().read(AES.block_size)
        s = '今天 10:00 AM'
        # ECB
        encrypter = tools.Encrypter(key)
        self.assertEqual(encrypter.decrypt(encrypter.encrypt(s)), s)
        # CBC
        encrypter = tools.Encrypter(key, AES.MODE_CBC, iv)
        self.assertEqual(encrypter.decrypt(encrypter.encrypt(s)), s)
        # CFB
        encrypter = tools.Encrypter(key, AES.MODE_CFB, iv)
        self.assertEqual(encrypter.decrypt(encrypter.encrypt(s)), s)
