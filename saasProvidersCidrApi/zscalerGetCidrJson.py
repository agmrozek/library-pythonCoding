import requests
from pprint import  pprint
import json

url = "https://api.config.zscaler.com/zscaler.net/cenr/json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint(data)
