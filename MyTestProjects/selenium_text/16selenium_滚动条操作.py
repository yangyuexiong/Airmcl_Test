from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.51zxw.net/')
sleep(2)

js = "var action=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(2)

js = "var action=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(3)

