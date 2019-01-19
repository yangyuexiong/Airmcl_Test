from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# 截图-得到截图保存为一个文件-设置路径
driver.get_screenshot_as_file \
    (r'C:\Users\Administrator\Desktop\api_01\selenium_text\baodu.jpg')
sleep(2)

driver.get('http://www.51zxw.net/')
driver.get_screenshot_as_file \
    (r'C:\Users\Administrator\Desktop\api_01\selenium_text\zxw.png')
