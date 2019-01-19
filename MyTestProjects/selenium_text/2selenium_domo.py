from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

#定位元素设置值
#driver.find_element_by_id('kw').send_keys('dnf')
driver.find_element_by_name('wd').send_keys('LOL')
sleep(2)

#点击
driver.find_element_by_id('su').click()
sleep(3)

driver.quit()