#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import hashlib
import operator
import random
import string
import time

from Crypto.Cipher import AES


def random_string(length=8):
    """
    随机字符串
    :param length:
    :return:
    """
    return ''.join([random.choice(string.letters) for _ in xrange(length)])


def random_number_string(length=8):
    """
    随机数字字符串
    :param length:
    :return:
    """
    return ''.join([random.choice(string.digits) for _ in xrange(length)])


def random_calendar_eid(length=32):
    """
    随机创建一个符合规则的eid
    :param length:
    :return:
    """
    return ''.join([random.choice('0123456789aAbBcCdDeEfF') for _ in xrange(length)])


def random_string_and_number(length=32):
    """
    随机字母和数字混合字符串
    :param length: 
    :return: 
    """
    return ''.join([random.choice(string.letters + string.digits) for _ in xrange(length)])


def random_number(min_num=1, max_num=100):
    """
    随机自然数
    :param min_num:
    :param max_num:
    :return:
    """
    return random.randint(min_num, max_num)


def random_chinese_string(length=8):
    """
    随机中文
    :param length:
    :return:
    """
    chars = map(unichr, range(0x4E00, 0x9FA6))

    return ''.join([random.choice(chars).encode('utf-8', 'ignore') for _ in range(length)])


def sort_by_value(d):
    """
    字典按照value排序
    http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    :param d: 
    :return: 返回的是一个包含一系列tuple的list
    """
    return sorted(d.items(), key=operator.itemgetter(1))


def get_random_shuffle_list(l):
    """
    从传入的list中获取到一个乱序的list
    :param l: 
    :return: 
    """
    temp_list = l[:]
    random.shuffle(temp_list)

    return temp_list


def md5(s):
    """
    字符串md5
    :param s:
    :return:
    """
    m = hashlib.md5()
    m.update(s)

    return m.hexdigest()


def current_time():
    """
    当前时间戳 s
    :return:
    """
    return int(time.time())


def current_time_millis():
    """
    当前时间戳 ms
    :return:
    """
    return int(round(time.time() * 1000))


def base64_urlsafe_decode(s):
    """
    base64 解码(urlsafe兼容模式)
    :return:
    """
    # 系统的urlsafe_b64decode方法不支持补'='
    s = s.replace('-', '+').replace('_', '/') + '=' * (len(s) % 4)
    return base64.b64decode(s)


class Encrypter(object):
    """
    加解密类
    """
    def __init__(self, key, mode=AES.MODE_ECB, iv=None):
        """
        初始化
        :param key:
        :param mode:
        :param iv:
        """
        self.key = key
        self.mode = mode
        self.bs = AES.block_size
        self.iv = '0' * self.bs if iv is None else iv

    def encrypt(self, plaintext):
        """
        加密
        :param plaintext:
        :return:
        """
        pad = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

        cipher = AES.new(self.key, self.mode, self.iv)

        return base64.b64encode(cipher.encrypt(pad(plaintext)))

    def decrypt(self, ciphertext):
        """
        解密
        :param ciphertext:
        :return:
        """
        unpad = lambda s: s[0:-ord(s[-1])]

        ciphertext = base64_urlsafe_decode(ciphertext)
        cipher = AES.new(self.key, self.mode, self.iv)

        return unpad(cipher.decrypt(ciphertext))
