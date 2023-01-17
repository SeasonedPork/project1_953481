import pandas as pd
import requests
from flask import Flask, request, jsonify, json, render_template, make_response
from flask_cors import CORS, cross_origin
from elasticsearch import Elasticsearch
from jikanpy import Jikan
from nltk import PorterStemmer, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from backEnd import main

jikan = Jikan()

# this is so cursed
app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'
anime_data = requests.get("https://api.jikan.moe/v4/anime", headers={'accept': 'application/json'})
anime_top_data = requests.get("https://api.jikan.moe/v4/top/anime?limit=5", headers={'accept': 'application/json'})
anime_json = anime_data.json()
anime_top_json = anime_top_data.json()
manga_data = requests.get("https://api.jikan.moe/v4/manga", headers={'accept': 'application/json'})
manga_top_data = requests.get("https://api.jikan.moe/v4/top/manga?limit=5", headers={'accept': 'application/json'})
manga_json = manga_data.json()
manga_top_json = manga_top_data.json()
es = Elasticsearch
bookmark_mal_id = [1, 3,5,6]
favourite_mal_id = [1, 3,6,7]
bookmark_manga_mal_id = [4, 5, 6]
favourite_manga_mal_id = [4, 5, 6]
search_title = []
search_synopsis = []


# this part is about connect to each other
@app.route("/dataentry", methods=["POST", "GET"])
def submitData():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        name = post_data.get('emailReg'),
        department = post_data.get('passwordReg')
        print(name)
        print(department)
        response_object['message'] = 'Data added!'
    return jsonify(response_object)


@app.route("/search", methods=["GET"])
def search():
    search_term = request.form.get('searchTerm')
    search_results = search_term
    if search_results == None:
        return "empty shell"
    else:
        return jsonify(search_results)

@app.route("/searchManga", methods=["GET"])
def search_M():
    search_term = request.form.get('searchTerm')
    search_results = search_term
    if search_results == None:
        return "empty shell"
    else:
        return jsonify(search_results)


@app.route("/get_All", methods=["GET"])
def All():
    response_object = {'ALL_status': 'success'}
    if request.method == "GET":
        all_url = anime_json
        return all_url
    return response_object


@app.route("/topAnime", methods=["GET"])
def top():
    response_object = {'TOP_status': 'success'}
    if request.method == "GET":
        data_top = anime_top_json
        return data_top
    return response_object


@app.route("/get_All_manga", methods=["GET"])
def All_M():
    response_object = {'ALL_status': 'success'}
    if request.method == "GET":
        all_url = manga_json
        return all_url
    return response_object


@app.route("/topManga", methods=["GET"])
def top_M():
    response_object = {'TOP_status': 'success'}
    if request.method == "GET":
        data_top = manga_top_json
        return data_top
    return response_object


# try to use jikanpy
@app.route("/EventDetailView:", methods=["GET"])
def find():
    response_object = {'TOP_status': 'success'}
    if request.method == "GET":
        data_top = anime_top_json
        return data_top
    return response_object


@app.route("/yoink_B_id", methods=["GET"])
def yoink():
    response_object = {'Yoink': 'success'}
    search_term = request.args.get('mal_id')
    convert_int = int(search_term)
    for i in bookmark_mal_id:
        if i != convert_int:
            bookmark_mal_id.append(convert_int)
    return bookmark_mal_id


@app.route("/yoink_fav", methods=["GET"])
def yoink_fav():
    response_object = {'Yoink': 'success'}
    search_term = request.args.get('mal_id')
    convert_int = int(search_term)
    for i in favourite_mal_id:
        if i != convert_int:
            favourite_mal_id.append(convert_int)
    return favourite_mal_id


@app.route("/yoink_manga_fav", methods=["GET"])
def yoink_manga_fav():
    response_object = {'Yoink': 'success'}
    search_term = request.args.get('mal_id')
    convert_int = int(search_term)
    for i in favourite_manga_mal_id:
        if i != convert_int:
            favourite_manga_mal_id.append(convert_int)
    return favourite_manga_mal_id


@app.route("/yoink_B_manga_id", methods=["GET"])
def yoink_manga():
    response_object = {'Yoink': 'success'}
    search_term = request.args.get('mal_id')
    convert_int = int(search_term)
    for i in bookmark_manga_mal_id:
        if i != convert_int:
            bookmark_manga_mal_id.append(convert_int)
    return bookmark_manga_mal_id

@app.route("/get_bookmark_anime", methods=["GET"])
def get_yoink_bookmark_anime():
    return jsonify(bookmark_mal_id)
@app.route("/get_fav_anime", methods=["GET"])
def get_yoink_anime():
    return jsonify(favourite_mal_id)
@app.route("/get_bookmark_manga", methods=["GET"])
def get_yoink_bookmark_manga():
    return jsonify(bookmark_manga_mal_id)
@app.route("/get_fav_manga", methods=["GET"])
def get_yoink_manga():
    return jsonify(favourite_manga_mal_id)
@app.route("/delete_anime_fav", methods=["GET"])
def delete_anime_fav():
    search_term = request.args.get('mal_id')
    convert_int = int(search_term)
    for i in favourite_mal_id:
        if i == convert_int:
            favourite_mal_id.remove(convert_int)
    return favourite_mal_id
@app.route("/delete_anime_bookmark", methods=["GET"])
def delete_anime_fav_bookmark():
    search_term = request.args.get('mal_id')
    convert_int = int(search_term)
    for i in bookmark_mal_id:
        if i == convert_int:
            bookmark_mal_id.remove(convert_int)
    return bookmark_mal_id

@app.route('/title', methods=['GET'])
def SearchByTitle():
    argList = request.args.to_dict(flat=False)
    query_term = argList['query'][0]
    result = search.searchByTitle(query_term)
    # check whether if result is a dataframe
    if isinstance(result, pd.DataFrame):
        resultTranpose = result.T
        jsonResult = resultTranpose.to_json()
        response = make_response(jsonResult)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    else:
        jsonResult = {'response': '404', 'similar': result}
        response = make_response(jsonResult)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

@app.route('/description', methods=['GET'])
def SearchByDescription():
    argList = request.args.to_dict(flat=False)
    query_term = argList['query'][0]
    result = search.searchByDescription(query_term)
    # check whether if result is a dataframe
    if isinstance(result, pd.DataFrame):
        resultTranpose = result.T
        jsonResult = resultTranpose.to_json()
        response = make_response(jsonResult)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    else:
        jsonResult = {'response': '404', 'similar': result}
        response = make_response(jsonResult)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response


if __name__ == '__main__':
    app.run(debug=True)
