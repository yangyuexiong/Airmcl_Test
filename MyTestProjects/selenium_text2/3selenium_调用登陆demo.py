from seleniumlogindemo import *
from selenium import webdriver
from time import sleep

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get('http://www.51zxw.net')
driver.implicitly_wait(10)

Login().usre_login(driver)
sleep(3)
Login().user_logout(driver)
driver.forward()
sleep(3)
driver.quit()
