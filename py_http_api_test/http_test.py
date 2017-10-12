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
    # 配置信息
    config = None
    # case执行环境（配置文件路径）
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
                if '-env=' in arg:
                    env = arg.split('=')[-1]
                # 获取nose的配置文件
                if '--config' in arg:
                    nose_cfg = arg.split('=')[-1]
                if '-c' in arg:
                    nose_cfg = argvs[idx + 1]
            # 尝试从用户指定或者工作目录下的nose配置文件中获取环境参数
            nose_config_files = nose.config.all_config_files()
            if env is None and (nose_cfg is not None or len(nose_config_files) > 0):
                if nose_cfg is None:
                    nose_cfg = nose_config_files[-1]
                if not os.path.isabs(nose_cfg):
                    nose_cfg = os.getcwd() + '/' + nose_cfg
                cf = ConfigParser.ConfigParser()
                cf.read(nose_cfg)
                try:
                    env = cf.get('others', 'env')
                except ConfigParser.Error:
                    env = None
            # 运行参数未传入而且有代码注入的配置文件路径
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
