from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
file_path=r'C:\Users\Administrator\Desktop\api_01\selenium_text\Franme.html'
driver.get(file_path)

#进入嵌套
driver.switch_to.frame('search')
driver.find_element_by_css_selector('#query').send_keys('dnf')
sleep(2)
driver.find_element_by_css_selector('#stb').click()


