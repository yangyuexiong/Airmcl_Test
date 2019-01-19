from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.51zxw.net/list.aspx?cid=615')

#定义变量获取窗口句柄
selenium_index=driver.current_window_handle
sleep(2)

#点击：2-1
driver.find_element_by_partial_link_text('2-1').click()
#返回
driver.switch_to.window(selenium_index)

#点击：3-1
driver.find_element_by_partial_link_text('3-1').click()
#返回
driver.switch_to.window(selenium_index)


