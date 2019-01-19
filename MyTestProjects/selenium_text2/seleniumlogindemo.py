from selenium import webdriver
from time import sleep


class Login():
    def usre_login(self, driver):
        driver.find_element_by_css_selector("[type='text']").clear()
        driver.find_element_by_css_selector("[type='text']").send_keys('z87254091')
        driver.find_element_by_css_selector("[type='password']").clear()
        driver.find_element_by_css_selector("[type='password']").send_keys('z87254091')
        driver.find_element_by_css_selector('form#loginForm>ul>input[value="登录"]').click()

    def user_logout(self, driver):
        driver.find_element_by_link_text('退出登录').click()
        sleep(2)
        # driver.switch_to_alert().accept()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # driver.get('https://www.baidu.com/')
    driver.get('http://www.51zxw.net')
    driver.implicitly_wait(10)

    Login().usre_login(driver)
    sleep(3)
    driver.forward()
    Login().user_logout(driver)
    sleep(2)
    # driver.quit()
