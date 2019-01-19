from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait     #显示等待元素
#条件用于显示等待 /EC简化用于调用时方便使用
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By   #等位元素
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(2)

driver.find_element_by_css_selector('#kw').send_keys('dnf')

#定义变量传入 对象/范围/5s每隔0.5s检测  直到元素是否呈现
element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
element.click()
