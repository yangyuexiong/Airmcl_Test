from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://www.51zxw.net')
#driver.get('http://www.baidu.com')


select = Select(driver.find_element_by_css_selector("[name='CookieDate']"))

#通过索引
#select.select_by_index(1)

#通过文字
#select.select_by_visible_text('留一年')

#通过值
select.select_by_value("1")


sleep(2)




