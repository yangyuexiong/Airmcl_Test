from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

driver.find_element_by_css_selector('.soutu-btn').click()
sleep(2)

#上传图片/进行搜索
driver.find_element_by_css_selector('.upload-pic').send_keys\
    (r'C:\Users\Administrator\Desktop\api_01\selenium_text\IMG_4190.JPG')
sleep(2)


