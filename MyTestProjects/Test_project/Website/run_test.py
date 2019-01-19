import unittest
from function import *
from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner
import time

# 报告路径
report_dir = './test_report'
# 测试路径
test_dir = './test_case'

print('开始执行用例')

# 测试路径，匹配规则
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')

# 时间拼接报告名称
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + '.html'
print('开始生成测试报告')

# 打开-生成测试报告
with open(report_name, 'wb') as f:
    print(f)
    runner = HTMLTestRunner(stream=f, title='测试报告', description='登陆模块')
    runner.run(discover)
    f.close()

print('查找最新报告')
latest_report = latest_report(report_dir)

print('发送报告到邮箱')
send_mail(latest_report)
