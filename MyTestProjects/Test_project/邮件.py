from email.header import Header
from email.mime.text import MIMEText
import smtplib


smtpserver = 'smtp.qq.com'
user = '872540033@qq.com'
password = 'enpjfrnsxuhqbffb'

# 发送
sender = '872540033@qq.com'
# 接收人
receive = '417993207@qq.com'

# 邮件标题-内容
subject = '自动化测试报告'
content = 'ok'

# 邮件正文
msg = MIMEText(content, 'html', 'utf-8')
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
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print('发送完成')

'''

['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', 
'/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', 
'/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', 
'/Users/yangyuexiong/Library/Python/3.6/lib/python/site-packages', 
'/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']

/Library/Frameworks/Python.framework/Versions/3.6/bin
'''