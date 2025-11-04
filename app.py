from  flask import Flask, jsonify
import requests
from flask_cors import CORS


BASE_URL='https://api.zeroc.green/v1/'

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def hello_world():
    response= requests.get(BASE_URL + 'stations/')
    data= response.json()
    stations=data.get('stations', [])
    return jsonify(stations)
    

    
