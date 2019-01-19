from selenium import webdriver
from time import sleep

#driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get('http://www.51zxw.net')

#driver.find_element_by_tag_name('input').send_keys('selenium')
#不精准定位方法
# driver.find_element_by_css_selector("[type='text']").send_keys('z87254091')
# driver.find_element_by_css_selector("[type='password']").send_keys('z87254091')

driver.find_element_by_name('username').send_keys('z87254091')
driver.find_element_by_name('password').send_keys('z87254091')
sleep(1)

driver.find_element_by_css_selector('form#loginForm>ul>input[value="登录"]').click()
sleep(5)
driver.forward()

driver.find_element_by_link_text('退出登录').click()


#driver.quit()

