from basepage import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


class LoginPage(Page):
    url = '/'

    # 定位
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.CSS_SELECTOR, '[type="submit"]')

    # 封装
    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def Login_action(self, username, password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    # 断言-判断用例是否成功/使用参照物
    loginPass_loc = (By.LINK_TEXT, '退出登录')
    loginFail_loc = (By.NAME, 'username')

    # 返回判断结果T/F
    def type_loginPass_hine(self):
        return self.find_element(*self.loginPass_loc).text

    # F
    def type_loginFail_hine(self):
        return self.find_element(*self.loginFail_loc).text
