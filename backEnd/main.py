import requests
import pandas as pd

response = requests.get('https://api.jikan.moe/v4/anime')
response_json = response.json()

# convert json to dataframe
df = pd.json_normalize(response_json)

# write dataframe to csv file
df.to_csv('../backEnd/resource/anime_data.csv', index=False)

df = df.T

# write dataframe to csv file
df.to_csv('../backEnd/resource/anime_data.csv', index=False)