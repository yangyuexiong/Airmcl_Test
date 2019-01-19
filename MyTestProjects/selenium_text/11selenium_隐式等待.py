from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime,sleep

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(2)

#隐式等待：所有等待不超过5s
driver.implicitly_wait(5)

try:
    print(ctime())
    driver.find_element_by_css_selector('#kw').send_keys('dnf')
    driver.find_element_by_css_selector('#su').click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())
