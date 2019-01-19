from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://www.51zxw.net/')

#获取cookie数据
cookie=driver.get_cookies()
print(cookie)
print(cookie[0])

#增加cookie属性
driver.add_cookie({'name':'51zxw',
                   'value':'www.51zxw.net'})
for cookie in driver.get_cookies():
    print("%s——%s" %(cookie['name'],cookie['value']))