from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

#增加
driver.add_cookie({'name':'BAIDUID',
                   'value':'EF8153A175A034F3CDAA2D9509823CEB:FG=1'})
driver.add_cookie(({'name':'BDUSS',
                    'value':'l3TkVCOE9iajZTQzRDT3FobTlIQ243NkdvNnJBb2ZaZ2NoeDg0cENIMG9vcHBaSVFBQUFBJCQAAAAAAAAAAAEAAAAvRT4Pejg3MjU0MDkxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgVc1koFXNZcn'}))
sleep(3)
driver.forward()


