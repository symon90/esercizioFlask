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

@app.route('/station/<station_id>', methods=['GET'])
def get_station(station_id):
    response= requests.get(BASE_URL + f'stations/{station_id}')
    data= response.json()
    data=modifyed_data(data)
    
    return jsonify(data)
    

    

def modifyed_data(data):
    for metric in data['metrics']:
        metric['data_points'] = metric['data_points'][-5:]
    
    return data