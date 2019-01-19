from selenium import webdriver
from selenium.webdriver.common.by import By

def ok():
    driver = webdriver.Firefox()

    driver.get('http://www.51zxw.net')

    driver.find_element_by_name('username').send_keys('z87254091')
    driver.find_element_by_name('password').send_keys('z87254091')
    driver.find_element_by_css_selector('[type="submit"]').click()

    # username_loc = (By.NAME, 'username')
    # password_loc = (By.NAME, 'password')
    # submit_loc = (By.CSS_SELECTOR, '[type="submit"]')
    #driver.maximize_window()
    return driver

if __name__ == '__main__':
    ok()


