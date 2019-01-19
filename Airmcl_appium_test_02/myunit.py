#!/usr/bin/env python
# encoding: utf-8

"""用例执行前后准备工作"""

from appium_config import appium_android
import unittest


# 测试环境准备
class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = appium_android()
        print('测试开始___________________________>')
        print('⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊-⇊', '\n')

    def tearDown(self):
        print('关闭app')
        # self.driver.close_app()
        print('测试结束___________________________>', '\n')
