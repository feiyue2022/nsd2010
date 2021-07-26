import requests
url = 'http://www.jianshu.com'
#如果python的模块请求被网站的robots协议拒绝，可以进行headers伪装
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
r = requests.get(url,headers=headers)
print(r.text)
