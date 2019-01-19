from url_case.request_func import *

interface_name = '1.登陆接口'

case_name = '用例1:正确手机-验证码'

url = "http://s.airbeauty.com.cn:8089/airbeautyone/appApiV2_2/customer/customer_login.do"

querystring = {"TEL": "15013038819", "VerifyCode": "2016"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "32e807f1-f8bb-de4b-602f-308e36247133"
}

q = url_request.get(url, querystring, headers)
print('q:', q)
z = url_request.r_result(q[0], q[1], interface_name)
print('z:', z)
# result_pass(z,case_name)
resule_fail(z, case_name)
