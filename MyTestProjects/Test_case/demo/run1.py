from urllib import request, parse
from urllib.error import URLError
import threading


class postRequest():
    def __init__(self, url, values, interface_name):
        self.url = url
        self.values = values
        self.interface_name = interface_name

    def post(self):
        parms = self.values
        querystring = parse.urlencode(parms)
        try:
            u = request.urlopen(self.url, querystring.encode('ascii'))
            resp = u.read()
            print(u"接口名字为：", self.interface_name)
            print(u"所传递的参数为：\n", parms)
            print(u"服务器返回值为：\n", resp)
        except URLError as e:
            print(e)


def Login():  # 定义接口函数
    # 实例化接口对象
    login = postRequest('http://127.0.0.1:5000/auth/login', {

        "mobile": 15013038819,
        "password": "123456"}, "1.login")
    return login.post()


try:
    i = 0
    tasks = []  # 任务列表
    task_number = 1
    while i < task_number:
        t = threading.Thread(target=Login)
        tasks.append(t)  # 加入线程池，按需使用
        t.start()  # 多线程并发
except Exception as e:
    print(e)
