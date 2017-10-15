#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_greater_equal
from nose.tools import assert_is_not_none
from nose.tools import eq_
from nosedep import depends

from py_http_api_test.http_test import HttpTest
from py_http_api_test.jmespath_custom import search as jq_


class ContactsApiTest(HttpTest):
    """
    通讯录接口测试
    https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.8zqGzC&treeId=172&articleId=104979&docType=1
    """
    access_token = None

    def test_gettoken(self):
        """
        获取access_token
        :return:
        """
        params = {
            'corpid': self.__class__.config['corpid'],
            'corpsecret': self.__class__.config['corpsecret']
        }

        response = self.__class__.http_session.request(
            'GET',
            self.__class__.config['dingtalk_oapi'] + '/gettoken',
            params=params
        ).json()

        self.__class__.access_token = jq_('access_token', response)

        eq_(jq_('errcode', response), 0)
        assert_is_not_none(self.__class__.access_token)

    @depends(after='test_gettoken')
    def test_department_list(self):
        """
        获取部门列表
        :return:
        """
        params = {
            'access_token': self.__class__.access_token,
            'id': self.__class__.config['department_parentid']
        }

        response = self.__class__.http_session.request(
            'GET',
            self.__class__.config['dingtalk_oapi'] + '/department/list',
            params=params
        ).json()

        eq_(jq_('errcode', response), 0)
        assert_greater_equal(len(jq_('department', response)), 1)
