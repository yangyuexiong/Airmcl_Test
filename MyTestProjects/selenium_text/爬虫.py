import urllib
import urllib.request
import re

def load_page(url):

    #请求网页里连接
    request=urllib.request.Request(url)

    #响应页面
    response=urllib.request.urlopen(request)
    data = response.read()
    return data

def get_image(html):

    #定义变量存储正则表达式
    regx=r'http://[\S]*jpg'

    pattern = re.compile(regx)

    #抓取出来的所有数据存放用于便利
    get_image = re.findall(pattern,repr(html))

    num = 1
    for img in get_image:
        image = load_page(img)
        with open('G:\\okc\\%s.jpg'%num,'wb') as fb:
            fb.write(image)
            print('正在下载地%s张图片'%num)
            num=num+1
    print('ok!')

url='http://mini.eastday.com/?qid=6789dh'

html=load_page(url)

get_image(html)



