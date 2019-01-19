from selenium import webdriver
import os

from email.header import Header
from email.mime.text import MIMEText
import smtplib


# 截图路径
def insert_img(driver, filename):
    func_path = os.path.dirname(__file__)  # 读取本路径
    # print(func_path)

    base_dir = os.path.dirname(func_path)  # 读取上一级路径
    # print(base_dir)

    # 转义成相对路径
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    # print(base_dir)

    base = base_dir.split('/Website')[0]
    # print(base)

    filepath = base + '/Website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(filepath)


# 查找最新报告
def latest_report(report_dir):
    lists = os.listdir(report_dir)  # 报告列表
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))  # 排序
    file = os.path.join(report_dir, lists[-1])  # 最新生成的报告
    return file


# 邮件
def send_mail(latest_report):
    f = open(latest_report, 'rb')  # 打开最新报告
    mail_content = f.read()  # 读取
    f.close()

    smtpserver = 'smtp.qq.com'
    user = '872540033@qq.com'
    password = 'enpjfrnsxuhqbffb'

    sender = '872540033@qq.com'
    receive = '417993207@qq.com'

    # 邮件标题-内容
    subject = '自动化测试报告'
    # 邮件正文
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receive
    # SSL协议端口号
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # 认证
    smtp.helo(smtpserver)  # 向服务器标识身份
    smtp.ehlo(smtpserver)  # 服务器返回结果确认
    smtp.login(user, password)  # 登录
    print('开始发送邮件')
    smtp.sendmail(sender, receive, msg.as_string())
    smtp.quit()
    print('发送完成')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    insert_img(driver, 'baidu.jpg')
