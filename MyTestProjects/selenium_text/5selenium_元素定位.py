from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

#文字元素定位
#完整的文字搜索
driver.find_element_by_link_text('地图').click()

#部分文字输入-模糊搜索
#driver.find_element_by_partial_link_text('图').click()


#driver.quit()

