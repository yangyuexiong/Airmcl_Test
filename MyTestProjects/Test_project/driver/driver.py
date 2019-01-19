from selenium import webdriver


def browser():
    driver = webdriver.Chrome()
    # driver=webdriver.Firefox()
    # driver=webdriver.Ie()
    # driver.get('https://www.baidu.com/')



    return driver


if __name__ == '__main__':
    browser()
