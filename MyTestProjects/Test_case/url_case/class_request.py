import requests
from urllib import request, parse
from urllib.error import URLError
import datetime
import time
import threading

error = []
err_msg = []


class url_request():
    def __init__(self, url, values, interface_name):
        self.url = url
        self.values = values
        self.interface_name = interface_name

    def open_url(self):
        parms = self.values
        # print('parms->>>:',parse)

        querystring = parse.urlencode(parms)
        # print('querystring->>>:',querystring)

        try:
            u = request.urlopen(self.url, querystring.encode('ascii'))

            resp = u.read()  # 读取二进制
            # print(type(resp))

            resp = resp.decode()  # 二进制转str
            # print(type(resp))

            resp = eval(resp)  # str转dict
            # print(type(resp))

            # print(">>>接口名字为:", self.interface_name,'!')
            # print(">>>所传递的参数为:", parms)
            # print(">>>服务器返回值为:", resp)

            # 取出元组取值
            resp = ('status', resp['status'])
            # print('resp:','status:',resp[1])
            n = resp[1]
            # print('n:',n)
            return n

        except URLError as e:
            print('请求失败:错误原因----->>>url_request():', '【', e, '】')
            error.append('0')
            err_msg.append(str(e))


def reuqest_go():
    try:
        r = url_request(url, values, interface_name)
        return r.open_url()

    except Exception as e:
        print('错误:--->>>', 'reuqest_go()请求数据出错>>>无法得到相应的值:', e)
        error.append('0')
        err_msg.append(str(e))


def r_result(v, x):
    # print('v',v)
    # print('i_n',x)
    try:
        if v == "OK" or v == 200:
            print(x, '>>>', '->>>并且返回:', v, '\n', '__________________________________________________')
            return v

        elif v == "ERROR" or type(v) == type(1):
            print(x, '>>>', '->>>并且返回:', v, '\n', '__________________________________________________')
            return v
        else:
            print(x, '>>>', '->>>没有定位到相关keys作出判断!!!', v)
            return v
    except BaseException as e:
        print(e)
        print(x, '>>>请求失败', 'r_result():错误原因----->>>', e)
        error.append('0')
        err_msg.append(str(e))


# 基本流
def result_pass(j, b):
    s = 'OK 或 200'

    if j == 'OK' or j == 200 or j != None:
        print('<', b, '>\n>>>', '期待返回状态:', s, '实际返回状态:<', j, '>:用例通过', '\n',
              '__________________________________________________')
    else:
        print('<', b, '>\n>>>', '期待返回状态:', s, '实际返回状态:<', j, '>:用例失败', '\n',
              '__________________________________________________')


# 备选流
def resule_fail(j, b):
    print('j:', j, type(j))

    s = 'ERROR 或 40X 或 None'

    x = range(1, 18)
    for i in x:
        k = 400 + i
        if j == None or j == 'ERROR' or (j != 200 and j == k):
            print('<', b, '>\n>>>', '1.期待返回状态:', s, '实际返回状态:<', j, '>:用例通过', '\n',
                  '__________________________________________________')
            break
    else:
        print('<', b, '>\n>>>', '2.期待返回状态:', s, '实际返回状态:<', j, '>:用例失败', '\n',
              '__________________________________________________')


if __name__ == '__main__':
    # get方式
    # url="http://test.sgj.airmcl.com:8090/airbeautyone/appApiV2_2/customer/customer_login.do"
    # "http://s.airbeauty.com.cn:8089/airbeautyone/appApiV2_2/customer/customer_login.do?TEL=15013038819&VerifyCode=2016"

    # url="http://s.airbeauty.com.cn:8089/airbeautyone/appApiV2_2/customer/customer_login.do"
    # values={"TEL": "15013038819", "VerifyCode": "2016"}

    # e89386592dd842a4aa9fe90a1ac364e7

    # post方式
    # ab -n 100 -c 100 -p /Users/yangyuexiong/Desktop/demo -T application/x-www-form-urlencoded http://127.0.0.1:5000/auth/login

    url = "http://127.0.0.1:5000/auth/login"
    values = {"mobile": "15013038819", "password": "123456"}

    interface_name = '1.登陆接口'

    case_name = '用例1:正确手机-验证码'

    x = reuqest_go()
    print('得到返回值:>>>', x)

    r_result(x, interface_name)

    result_pass(x, case_name)

    # resule_fail(x,case_name)

'''_______________________________'''

try:
    x = reuqest_go
    # print('xxxxxx',x)

    tasks = []  # 任务列表

    starttime = datetime.datetime.now()  # 开始时间
    print("开始时间:", starttime)

    task_number = 1000  # 并发次数

    ThinkTime = 0  # 设置思考时间

    for i in range(1, task_number + 1):
        t = threading.Thread(target=x)
        # print('tttttt',t)

        tasks.append(t)  # 加入线程池，按需使用
    # print('任务list：',tasks)
    print('_______________________________')

    for t in tasks:
        time.sleep(ThinkTime)
        # print('tasks',tasks) # 打印线程

        t.setDaemon(True)
        t.start()
        # print(datetime.datetime.now(), t.getName())

    for t in tasks:  # 等待所有任务执行完毕
        t.join()
        # print('end', datetime.datetime.now(), t.getName())

        # print('所有任务执行完毕',datetime.datetime.now())

except Exception as e:
    print(e)

endtime = datetime.datetime.now()
print('结束时间:', endtime)
print('___________________________')

# 计算数组的平均值，保留3位小数
# AverageTime = "{:.3f}".format(float(sum(x.times))/float(len(x.times)))
# print("平均响应时间 %s ms" %AverageTime) #打印平均响应时间

# 计算总的思考时间+请求时间
usetime = str(endtime - starttime)
hour = usetime.split(':').pop(0)
minute = usetime.split(':').pop(1)
second = usetime.split(':').pop(2)
totaltime = float(hour) * 60 * 60 + float(minute) * 60 + float(second)

# 打印并发数
print("并发数:{}".format(task_number))

# 打印总共消耗的时间
print("总共消耗的时间 %s s" % (totaltime - float(task_number * ThinkTime)))

# 打印错误请求数
e_num = error.count('0') - 1
print("错误请求数:", int(e_num))

# 报错明细
new_err_msg = []
for i in err_msg:
    if i not in new_err_msg:
        new_err_msg.append(i)

if new_err_msg == []:
    print(">>>无错误信息!!!")

else:
    print(">>>错误信息集↓↓↓↓↓↓↓:")
    for i in new_err_msg:
        print(i + '\n')
