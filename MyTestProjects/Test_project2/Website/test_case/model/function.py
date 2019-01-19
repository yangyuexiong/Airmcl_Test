from selenium import webdriver
import os

#截图路径
def insert_img(driver,filename):
    func_path=os.path.dirname(__file__)#读取本路径
    print(func_path)

    base_dir=os.path.dirname(func_path)#读取上一级路径
    print(base_dir)

    #转义成相对路径
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    print(base_dir)

    base=base_dir.split('/Website')[0]
    print(base)

    filepath=base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)

#邮件


if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    insert_img(driver,'baidu.jpg')

