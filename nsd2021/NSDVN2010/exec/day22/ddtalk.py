import requests
import json
def bcrobot(url,data):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    r = requests.post(url=url,headers=headers,data=json.dumps(data))
    return r.json()
if __name__ == '__main__':
    url = 'https://oapi.dingtalk.com/robot/send?access_token=f94d1353962981faf3c37d1fe580e129aa0b2af3d920a8118580ecd6c769882b'
    # data = {
    #     "at": {
    #         "isAtAll": False
    #     },
    #     "text": {
    #         "content":"我就是我, @XXX 是不一样的烟火,python"
    #     },
    #     "msgtype":"text"
    # }
    data  = {
     "msgtype": "markdown",
     "markdown": {
         "title":"杭州天气",
         "text": "#### 杭州天气 @150XXXXXXXX \n > python 9度，西北风1级，空气良89，相对温度73%\n > ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n > ###### 10点20分发布 [天气](https://www.baidu.com/) \n"
     },
      "at": {
            "isAtAll": False
        }
    }
    res = bcrobot(url,data)
    print(res)