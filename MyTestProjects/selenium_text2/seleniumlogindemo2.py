from selenium import webdriver
from time import sleep


class Login():
    def usre_login(self, driver, username, password):
        driver.find_element_by_css_selector("[type='text']").clear()
        driver.find_element_by_name('username').send_keys(username)

        driver.find_element_by_css_selector("[type='password']").clear()
        driver.find_element_by_name('password').send_keys(password)

        driver.find_element_by_css_selector('form#loginForm>ul>input[value="登录"]').click()

    def user_logout(self, driver):
        driver.find_element_by_link_text('退出登录').click()
        sleep(2)
        # driver.switch_to_alert().accept()


if __name__ == '__main__':
    pass
