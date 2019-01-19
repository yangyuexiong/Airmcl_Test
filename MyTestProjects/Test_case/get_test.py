import requests
import json

url = "http://s.airbeauty.com.cn:8089/airbeautyone/appApiV2_2/customer/customer_login.do"

querystring = {"TEL": "15013038819", "VerifyCode": "2016"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "32e807f1-f8bb-de4b-602f-308e36247133"
}

# response = requests.request("GET", url, headers=headers, params=querystring)
response = requests.get(url, headers=headers, params=querystring)

# 转dict
s = json.loads(response.text)
print('s', type(s), s)

# 取出元组
a = ('status', s['status'])
print(type(a), a)
print(a[0])

# list-->>元组[0]
# s=sorted(s.items())
# print('s',type(s))

# print('s',type(s),s)
# print(s[1])

# 取value
# v=s.values()
# print(v)
#
# g=list(v)
# print(type(g),g[0])

# 转str
# b=json.dumps(s)
# print(type(b),b)
# print(b[0])


'''——————————————————————————————————————————————————————'''

try:
    if a[1] == "OK":
        print('1.登陆接口>>>请求成功', response, '->>>并且返回：登陆成功')

    elif a[1] == "ERROR":
        print('1.登陆接口>>>请求成功', response, '->>>并且返回：密码错误')
    else:
        print('1.登陆接口>>>请求成功', response, '->>>没有定位到相关keys作出判断!!!')

except Exception as e:
    print('1.登陆接口>>>请求失败:', e)
