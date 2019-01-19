import unittest
from model import myunit, function
from page_object.loginpage import *
from time import sleep


# 登录模块-测试用例
class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        '''1.正确的用户名与密码'''
        print('正在执行->>>用例：1.正确的用户名与密码')
        po = LoginPage(self.driver)
        po.Login_action('z87254091', 'z87254091')
        sleep(5)

        # 断言判断
        self.assertEqual(po.type_loginPass_hine(), '退出登录')
        # 截图
        function.insert_img(self.driver, '登陆成功.jpg')
        print('用例：1.正确的用户名与密码->>>执行完毕')

    @unittest.skip('ok')
    def test_login2_passwError(self):
        '''2.错误的密码'''
        print('正在执行->>>用例：2.错误的密码')
        po = LoginPage(self.driver)
        po.Login_action('z87254091', '000000')
        sleep(5)

        self.assertEqual(po.type_loginFail_hine(), '')
        function.insert_img(self.driver, '登陆失败.jpg')
        print('用例：2.错误的密码->>>执行完毕')

    @unittest.skip('ok')
    def test_login3_empty(self):
        '''3.帐号/密码为空'''
        print('正在执行->>>用例：3.帐号/密码为空')
        po = LoginPage(self.driver)
        po.Login_action('', '')
        sleep(5)

        self.assertEqual(po.type_loginFail_hine(), '')
        function.insert_img(self.driver, '登陆失败2.jpg')
        print('用例：3.帐号/密码为空->>>执行完毕')


if __name__ == '__main__':
    unittest.main()
