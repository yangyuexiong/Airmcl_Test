from time import sleep


class Page():
    '''页面基础类'''

    # 初始化
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://www.51zxw.net'
        self.timeout = 10

    def _open(self, url):
        url_ = self.base_url + url
        print('本次测试的url %s' % url_)
        self.driver.get(url_)
        self.driver.maximize_window()
        sleep(2)
        assert self.driver.current_url == url_, '%s' % url_

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
