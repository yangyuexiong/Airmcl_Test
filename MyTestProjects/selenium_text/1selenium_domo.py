from selenium import webdriver
from time import sleep
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#http://www.seleniumhq.org/
#binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
#driver = webdriver.Firefox(firefox_binary=binary)

#加载浏览器
#driver = webdriver.Firefox()
driver = webdriver.Chrome()

#打开url
driver.get('http://www.51zxw.net')
print(driver.title)
#最大化窗口
driver.maximize_window()
sleep(2)

driver.get('http://www.51zxw.net/list.aspx?cid=615')
print(driver.title)
#重置窗口大小
driver.set_window_size(400,800)
#刷新
driver.refresh()
sleep(2)

#返回上一层（后退按钮）
driver.forward()
sleep(3)

#关闭浏览器
driver.quit()