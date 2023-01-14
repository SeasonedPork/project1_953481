import json

import requests
import pandas as pd

response = requests.get('https://api.jikan.moe/v4/anime')
response_json = response.json()

df = pd.json_normalize(response_json)
df.to_csv('../backEnd/resource/anime_data.csv')
print("done")
