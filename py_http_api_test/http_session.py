#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
# 屏蔽https安全警告
# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import SNIMissingWarning
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(SNIMissingWarning)


class HttpSession(requests.Session):
    """
    http请求会话
    """

    def __init__(self):
        super(HttpSession, self).__init__()
        # 不校验SSL证书
        self.verify = False
        # 超时时间
        self.timeout = (60, 600)

    def update_cookies(self, cookies):
        """
        更新当前会话cookie
        :param cookies: cookie字典
        """
        requests.utils.add_dict_to_cookiejar(self.cookies, cookies)

    def update_headers(self, headers):
        """
        更新当前会话的header
        :param headers: header字典
        """
        self.headers.update(headers)
