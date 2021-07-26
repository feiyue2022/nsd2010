import requests
import json
from pprint import pprint

url = 'http://192.168.193.151/api_jsonrpc.php'
headers = {'Content-Type':'application/json-rpc;charset=utf-8'}
data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
    },
    "auth": "e71bca94536b09085068ef979bbff014",
    "id": 1
}

r = requests.post(url=url, headers=headers, data=json.dumps(data))
pprint(r.json())