import requests
import json

url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
response = requests.get(url)
data = json.loads(response.text)

for prefix in data['prefixes']:
    print(prefix['ip_prefix'])
