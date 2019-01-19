import unittest
from driver import browser


# 测试环境准备
class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        print('测试开始')

    def tearDown(self):
        self.driver.quit()
        print('测试完成')
