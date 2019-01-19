from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_link_text('设置').click()
sleep(2)
driver.find_element_by_link_text('搜索设置').click()
sleep(2)

driver.find_element_by_link_text('保存设置').click()

#定义变量存储弹窗
alter=driver.switch_to_alert()
#确认
alter.accept()