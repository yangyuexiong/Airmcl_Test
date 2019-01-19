from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.51zxw.net')
#driver.get('http://www.baidu.com')

#css ID的定位
# driver.find_element_by_css_selector('#kw').send_keys('dnf')

#css class的定位
#driver.find_element_by_css_selector('.s_ipt').send_keys('lol')

#css 属性的定位
#driver.find_element_by_css_selector("[autocomplete='off']").send_keys('lol')


#css 属性定位/设置
driver.find_element_by_css_selector('form#loginForm>ul>input[name="username"]').send_keys('z87254091')
sleep(1)
driver.find_element_by_css_selector('form#loginForm>ul>input[name="password"]').send_keys('z87254091')
sleep(1)

#下拉框定位选择-存在一个列表中s
#driver.find_elements_by_tag_name('option')[1].click()

#css 属性方式 !s
driver.find_element_by_css_selector('[value="1"]').click()

driver.find_element_by_css_selector('form#loginForm>ul>input[class="lobtn"]').click()

driver.forward()




