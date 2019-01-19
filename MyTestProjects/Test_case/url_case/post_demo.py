from url_case.request_func import *

interface_name = '1.登陆接口'

case_name = '用例1:正确手机-密码错误'

url = "http://127.0.0.1:5000/auth/login"

querystring = {"mobile": "15013038819", "password": "123456"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "32e807f1-f8bb-de4b-602f-308e36247133"
}

q = url_request.post(url, querystring, headers)
print('q:', q)
z = url_request.r_result(q[0], q[1], interface_name)
print('z:', z)
# result_pass(z,case_name)
resule_fail(z, case_name)
