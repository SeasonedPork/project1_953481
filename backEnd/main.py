import csv
import string
import pandas as pd
import requests as requests
import numpy as np
from bs4 import BeautifulSoup


def wrote_data():
    html_data = requests.get("https://api.jikan.moe/v4/anime", headers={'accept': 'application/json'})
    response_json = html_data.json()
    # orders =[ 'mal_id', 'title', 'type', 'score', 'scored_by', 'status', 'episodes', 'aired_from', 'aired_to', 'source',
    #      'members', 'favorites', 'duration', 'rating', 'nsfw', 'pending_approval', 'premiered_season', 'premiered_year',
    #      'broadcast_day', 'broadcast_time', 'genres', 'themes', 'demographics', 'studios', 'producers', 'licensors',
    #      'synopsis', 'background', 'main_picture', 'url', 'trailer_url', 'title_english', 'title_japanese', 'title_synonyms']
    #
    # df = pd.DataFrame.sort_values(by=orders)
    something = response_json["data"][4]
    print(something)



if __name__ == '__main__':
    wrote_data()
