import requests
from flask import Flask, request, jsonify, json,render_template
from flask_cors import CORS, cross_origin
from ElasticSearch_Oof import search

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'
anime_data = requests.get("https://api.jikan.moe/v4/anime", headers={'accept': 'application/json'})
anime_json = anime_data.json()
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
@app.route("/get_Image",methods=["POST"])
def Image(id):
    response_object = {'Image_status': 'success'}
    if request.method == "POST":
        pic_url = anime_json["images"]["jpg"]["image_url"][id]
        return pic_url
    return  response_object
@app.route("/get_All",methods=["GET"])
def All():
        all_url = anime_json
        return jsonify(all_url)




if __name__ == '__main__':
    app.run(debug=True)
