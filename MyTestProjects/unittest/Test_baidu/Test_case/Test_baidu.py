from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('开始测试>>>>>>>>>>>>>>>>>>')
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com')

    def test_baidu(self):
        '''百度'''
        driver = self.driver
        driver.find_element(By.ID, 'kw').clear()
        driver.find_element_by_id('kw').send_keys('dnf')
        driver.find_element_by_id('su').click()
        sleep(3)

        title = driver.title
        self.assertEqual(title, 'dnf_百度搜索')

        driver.find_element_by_partial_link_text('DNF').click()
        sleep(3)

    @classmethod
    def tearDownClass(self):
        self.driver.forward()
        self.driver.quit()
        print('结束测试>>>>>>>>>>>>>>>>>>')


if __name__ == '__main__':
    unittest.main()
