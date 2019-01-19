from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

#class属性定位
driver.find_element_by_class_name('s_ipt').send_keys('dnf')
sleep(5)
driver.find_element_by_id('su').click()



#driver.quit()

