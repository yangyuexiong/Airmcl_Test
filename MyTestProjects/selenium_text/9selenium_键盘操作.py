from selenium import webdriver
from time import sleep
from  selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_css_selector('#kw').send_keys('dnf')
sleep(2)

                                            #设置键盘指令/参数
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')
sleep(2)

#键盘指令
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')
#driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'x')


driver.get('https://www.sogou.com/')
sleep(2)
driver.find_element_by_css_selector('.sec-input').send_keys(Keys.CONTROL,'v')
sleep(2)
driver.find_element_by_css_selector('#stb').click()