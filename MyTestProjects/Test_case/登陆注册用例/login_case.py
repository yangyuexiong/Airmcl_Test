from url_case.request_func import *

interface_name = '1.登陆接口'

case_name='用例1:正确手机-验证码'

url = "http://s.airbeauty.com.cn:8089/airbeautyone/appApiV2_2/customer/customer_login.do"

querystring = {"TEL": "15013038819", "VerifyCode": "2016"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "32e807f1-f8bb-de4b-602f-308e36247133"
}

d = url_request.reqs(url, querystring, headers)
# print(d)
z = url_request.r_result(d[0], d[1], interface_name)
# print(z)
t_or_f(z,case_name)
