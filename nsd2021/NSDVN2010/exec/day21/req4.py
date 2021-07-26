import requests
from pprint import pprint

url='http://www.kuaidi100.com/query?'
params = {
    'type': 'youzhengguonei',
    'postid': '9893442769997'
}
r = requests.get(url,params=params)
pprint(r.json())