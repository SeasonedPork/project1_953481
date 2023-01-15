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
def get_and_clean_data():
    data = pd.read_csv('resource/software_developer_united_states_1971.csv')
    description = data['job_description']
    cleaned_description = description.apply(lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
    cleaned_description = cleaned_description.apply(lambda s: s.lower())
    cleaned_description = cleaned_description.apply(
        lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))
    cleaned_description = cleaned_description.drop_duplicates()
    return cleaned_description
