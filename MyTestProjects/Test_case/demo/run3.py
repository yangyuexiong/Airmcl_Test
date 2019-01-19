#!/user/bin/env python
# coding=utf-8
import requests
import datetime
import time
import threading


class url_request():
    times = []
    error = []

    def req(self, url):
        myreq = url_request(r)

        r = requests.post("http://127.0.0.1:5000/auth/login", )

        ResponseTime = float(r.elapsed.microseconds) / 1000  # 获取响应时间，单位ms
        myreq.times.append(ResponseTime)  # 将响应时间写入数组
        if r.status_code != 200:
            myreq.error.append("0")


if __name__ == '__main__':
    myreq = url_request()
    threads = []  # 线程
    starttime = datetime.datetime.now()  # 开始时间
    print("开始时间 %s" % starttime)

    nub = 1  # 设置并发线程数

    ThinkTime = 0.5  # 设置思考时间

    for i in range(1, nub + 1):
        t = threading.Thread(target=myreq.req, args=())
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        # print "thread %s" %t #打印线程
        t.setDaemon(True)
        t.start()

    t.join()  # 终止线程

    print('终止线程')
    endtime = datetime.datetime.now()  # 结束时间
    print("结束时间 %s" % endtime)
    time.sleep(3)

    AverageTime = "{:.3f}".format(float(sum(myreq.times)) / float(len(myreq.times)))  # 计算数组的平均值，保留3位小数
    print("平均响应时间 %s ms" % AverageTime)  # 打印平均响应时间

    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour) * 60 * 60 + float(minute) * 60 + float(second)  # 计算总的思考时间+请求时间

    print("并发数 %s" % nub)  # 打印并发数
    print("一共消耗的时间 %s s" % (totaltime - float(nub * ThinkTime)))  # 打印总共消耗的时间
    print("错误请求数 %s" % myreq.error.count("0"))  # 打印错误请求数
