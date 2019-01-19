import requests, parse
import json
import threading


class url_request(object):
    def get(url, querystring, headers):
        try:
            response = requests.get(url=url, headers=headers, params=querystring)
            # print(response)
            n = json.loads(response.text)
            n = ('status', n['status'])
            n = n[1]
            return (n, response)
        except BaseException as e:
            print('请求失败', response, ':错误原因----->>>', e)

    def post(url, querystring, headers):
        try:
            response = requests.post(url=url, headers=headers, data=querystring)
            n = json.loads(response.text)
            n = ('status', n['status'])
            n = n[1]
            return (n, response)
        except Exception as e:
            print('请求失败', response, ':错误原因----->>>', e)

    def r_result(v, y, x):
        # print('v',v)
        # print('y',y)
        # print('i_n',x)
        try:
            if v == "OK" or v == 200:
                print(x, '>>>', y, '->>>并且返回:', v, '\n', '__________________________________________________')
                return v

            elif v == "ERROR" or type(v) == type(1):
                print(x, '>>>', y, '->>>并且返回:', v, '\n', '__________________________________________________')
                return v
            else:
                print(x, '>>>', y, '->>>没有定位到相关keys作出判断!!!', v)
                return v
        except BaseException as e:
            print(e)
            print(x, '>>>请求失败', y, ':错误原因----->>>', e)


# 基本流
def result_pass(j, b):
    s = 'OK 或 200'

    if j == 'OK' or j == 200:
        print('<', b, '>\n>>>', '期待返回状态:', s, '实际返回状态:<', j, '>:用例通过', '\n',
              '__________________________________________________')
    else:
        print('<', b, '>\n>>>', '期待返回状态:', s, '实际返回状态:<', j, '>:用例失败', '\n',
              '__________________________________________________')


# 备选流
def resule_fail(j, b):
    s = 'ERROR 或 40X'

    if j == 'ERROR' or type(j) == type(1) and j != 200:
        print('<', b, '>\n>>>', '期待返回状态:', s, '实际返回状态:<', j, '>:用例通过', '\n',
              '__________________________________________________')
    else:
        print('<', b, '>\n>>>', '期待返回状态:', s, '实际返回状态:<', j, '>:用例失败', '\n',
              '__________________________________________________')


if __name__ == '__main__':
    interface_name = '1.登陆接口'

    case_name = '用例1:正确手机-验证码'

    url = "http://s.airbeauty.com.cn:8089/airbeautyone/appApiV2_2/customer/customer_login.do"

    # url = "https://huodong.lagou.com/activityapi/employer/signUp?companyId=107074"

    querystring = {"TEL": "15013038819", "VerifyCode": "20160"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "32e807f1-f8bb-de4b-602f-308e36247133"
    }

    q = url_request.get(url, querystring, headers)
    print(q)

    # z = url_request.r_result(q[0], q[1], interface_name)
    # print(z)
    # result_pass(z, case_name)
    # resule_fail(z,case_name)
