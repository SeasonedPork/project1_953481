import requests
from flask import Flask, request, jsonify, json,render_template
from flask_cors import CORS, cross_origin
from elasticsearch import Elasticsearch
from jikanpy import Jikan
from nltk import PorterStemmer, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from backEnd import main

jikan = Jikan()


app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'
anime_data = requests.get("https://api.jikan.moe/v4/anime", headers={'accept': 'application/json'})
anime_top_data = requests.get("https://api.jikan.moe/v4/top/anime?limit=5", headers={'accept': 'application/json'})
anime_json = anime_data.json()
anime_top_json = anime_top_data.json()
es = Elasticsearch
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

@app.route("/search", methods=["POST","GET"])
def search():
    response_object = {'Search_status': 'success'}
    if request.method == "POST":
        # search_input = request.form.get("search_input")
        # search(search_input)
        # # this is so curse HELP
        # result_s = search
        post_data = request.get_json()
        searchthing = post_data.get('S_input'),
        return searchthing
    return jsonify(response_object)

@app.route("/get_All",methods=["GET"])
def All():
    response_object = {'ALL_status': 'success'}
    if request.method == "GET":
        all_url = anime_json
        return all_url
    return response_object

@app.route("/topAnime",methods=["GET"])
def top():
    response_object = {'TOP_status': 'success'}
    if request.method == "GET":
        data_top = anime_top_json
        return data_top
    return response_object
#try to use jikanpy
@app.route("/EventDetailView:",methods=["GET"])
def find(name):
    response_object = {'TOP_status': 'success'}
    if request.method == "GET":
        data_top = anime_top_json
        return data_top
    return response_object

def preProcess(s):
    ps = PorterStemmer()
    s = word_tokenize(s)
    stopwords_set = set(stopwords.words())
    s = [w for w in s if w not in stopwords_set]
    # s = [w for w in s if not w.isdigit()]
    s = [ps.stem(w) for w in s]
    s = ' '.join(s)
    return s


def sk_vectorize():
    print("bag of words processing...")
    cleaned_description = main.get_and_clean_data()
    vectorizer = CountVectorizer(preprocessor=preProcess)
    vectorizer.fit(cleaned_description)
    vectorizer = CountVectorizer(preprocessor=preProcess, ngram_range=(1, 2))
    X = vectorizer.fit_transform(cleaned_description)





if __name__ == '__main__':
    app.run(debug=True)
