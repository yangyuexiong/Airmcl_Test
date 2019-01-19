#!/usr/bin/env python
# encoding: utf-8
from class_request import *

url = "http://s.airbeauty.com.cn:8089/airbeautyone/appApiV2_2/customer/customer_login.do"
values = {"TEL": "15013038819", "VerifyCode": "2016"}
interface_name = '1.登陆接口'
case_name = '用例1:正确手机-验证码'

r = url_request(url, values, interface_name)
r.open_url()




# r_result(x,interface_name)

# result_pass(x,case_name)
