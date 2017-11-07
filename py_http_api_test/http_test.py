#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os
import sys
import unittest

import nose.config
import ruamel.yaml

from py_http_api_test.http_session import HttpSession


class HttpTest(unittest.TestCase):
    """
    http接口测试类
    """
    # case配置信息(执行环境)
    config = None
    # case配置文件路径
    env = None
    # http会话对象
    http_session = HttpSession()

    def __init__(self, *args, **kwargs):
        """
        初始化公有变量
        :return:
        """
        unittest.TestCase.__init__(self, *args, **kwargs)

        if self.__class__.config is None:
            env = None
            nose_cfg = None
            argvs = sys.argv[1:]
            for idx, arg in enumerate(argvs):
                # 直接获取case配置文件路径
                if '-env=' in arg:
                    env = arg.split('=')[-1]
                    break
                # 获取nose的配置文件
                if '--config=' in arg:
                    nose_cfg = arg.split('=')[-1]
                if '-c' == arg:
                    nose_cfg = argvs[idx + 1]
            # 未获取到case配置文件路径，尝试从nose配置文件中获取
            nose_config_files = nose.config.all_config_files()
            if env is None and (nose_cfg is not None or len(nose_config_files) > 0):
                if nose_cfg is None:
                    # 用户未指定nose配置文件，则从系统全局配置文件中获取
                    nose_cfg = nose_config_files[-1]
                if not os.path.isabs(nose_cfg):
                    nose_cfg = os.getcwd() + '/' + nose_cfg
                cf = ConfigParser.ConfigParser()
                cf.read(nose_cfg)
                try:
                    env = cf.get('others', 'env')
                except ConfigParser.Error:
                    env = None
            # 未获取到case配置文件路径，但测试类中有定义
            if env is None and self.env is not None:
                env = self.env

            if env is not None:
                # 参数不是绝对路径
                if not os.path.isabs(env):
                    # 根据当前工作路径获取到绝对路径
                    env = os.getcwd() + '/' + env
                with open(env) as f:
                    inp = f.read()
                self.__class__.config = ruamel.yaml.safe_load(inp)
