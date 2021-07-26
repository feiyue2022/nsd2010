import requests
import json

url = 'http://192.168.193.151/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1,
}

r = requests.post(url=url,headers=headers,data=json.dumps(data))
print(r.json())