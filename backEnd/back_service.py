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
        print(name)
        print(department)
        response_object['message'] = 'Data added!'
    return jsonify(response_object)

@app.route("/search", methods=["POST","GET"])
def search():
    response_object = {'status': 'success'}
    if request.method == "POST":
        # search_input = request.form.get("search_input")
        # search(search_input)
        # # this is so curse HELP
        # result_s = search
        post_data = request.get_json()
        searchthing = post_data.get('S_input'),
        return searchthing
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True)
