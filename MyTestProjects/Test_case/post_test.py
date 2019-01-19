import requests
import json

url = "http://127.0.0.1:5000/auth/login"

payload = {"mobile": "15013038819", "password": "123456"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "32e807f1-f8bb-de4b-602f-308e36247133"
}

try:
    response = requests.post(url, data=payload, headers=headers)
    s = json.loads(response.text)
    # print(type(s),s)
    a = ('status', s['status'])
except Exception as e:
    print(e)

try:
    if a[1] == 200:
        print('1.登陆接口>>>请求成功', response, '->>>并且返回：登陆成功')

    elif a[1] == 404:
        print('1.登陆接口>>>请求成功', response, '->>>并且返回：密码错误')
    elif a[1] == 403:
        print('1.登陆接口>>>请求成功', response, '->>>并且返回：手机未注册')

    else:
        print('1.登陆接口>>>请求成功', response, '->>>没有定位到相关keys作出判断!!!')

except Exception as e:
    print('1.登陆接口>>>请求失败:', e)
