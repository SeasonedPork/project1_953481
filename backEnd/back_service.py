from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin
from ElasticSearch_Oof import search

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/dataentry", methods=["POST", "GET"])
def submitData():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        name = post_data.get('emailReg'),
        department = post_data.get('passwordReg')

        response_object['message'] = 'Data added!'
    return jsonify(response_object)

@app.route("/search", methods=["POST","GET"])
def search():
    response_object = {'status': 'success'}
    if request.method == "GET":


    return

if __name__ == '__main__':
    app.run(debug=True)
