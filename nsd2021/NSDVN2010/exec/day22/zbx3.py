import requests
import json

url = 'http://192.168.193.151/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc;charset=utf-8'}
data = {
    'jsonrpc': '2.0',
    'id': 1,
    'auth': 'e71bca94536b09085068ef979bbff014',
    'method': 'host.get',
    'params': {
        'output': ['hostid','host'],
        'selectInterfaces': ["interfaceid",'ip']
    }
}

r = requests.post(url=url,headers=headers,data=json.dumps(data))
print(r.json())