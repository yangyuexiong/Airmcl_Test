from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
#driver.get('http://www.51zxw.net')
driver.get('http://www.baidu.com')
driver.maximize_window()

driver.find_element_by_css_selector('#kw').send_keys('dnf')

#定义变量
element=driver.find_element_by_css_selector('#kw')
sleep(3)

#双击操作-传入变量存好的定位
ActionChains(driver).double_click(element).perform()
sleep(2)

#右键操作
ActionChains(driver).context_click(element).perform()

#鼠标悬停
#变量接收定位元素
above=driver.find_element_by_css_selector('.pf')
#传入变量
ActionChains(driver).move_to_element(above).perform()

driver.forward()



