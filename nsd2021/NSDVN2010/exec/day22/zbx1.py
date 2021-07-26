import requests
import json

url = 'http://192.168.193.151/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc;charset=utf-8'}
data = {
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": [],
    "id": 1
}

r = requests.post(url=url,headers=headers,data=json.dumps(data))
print(r.json())