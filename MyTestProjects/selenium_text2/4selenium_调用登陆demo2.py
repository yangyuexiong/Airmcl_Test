from seleniumlogindemo2 import *
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.51zxw.net')
driver.implicitly_wait(10)

Login().usre_login(driver, 'z87254091', 'z87254091')
sleep(3)
Login().user_logout(driver)

Login().usre_login(driver, 'a87254091', 'a87254091')
sleep(3)
driver.quit()
# Login().user_logout(driver)
