import json

import requests
import pandas as pd

response = requests.get('https://api.jikan.moe/v4/anime?q=')
response_json = response.json()


data_fix = json.dumps(response_json, indent=2,sort_keys=True)
print(type(data_fix))
print(type(response_json))
data_Json = json.loads(data_fix)
print(type(data_Json))

