from loginpage11 import *
from selenium import webdriver

driver = webdriver.Chrome()

username = 'z87254091'
password = 'z87254091'

test_user_login(driver, username, password)
sleep(3)
