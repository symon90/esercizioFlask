from  flask import Flask, jsonify
import requests
from flask_cors import CORS
from googletrans import Translator



BASE_URL='https://api.zeroc.green/v1/'

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/stations', methods=['GET'])
def hello_world():
    response= requests.get(BASE_URL + 'stations/')
    data= response.json()
    stations=data.get('stations', [])
    return jsonify(stations)

@app.route('/api/stations/<station_id>', methods=['GET'])
def get_station(station_id):
    response= requests.get(BASE_URL + f'stations/{station_id}')
    data= response.json()
    data=modifyed_data(data)
    
    return jsonify(data)
    

    
# modifica del json per mostrare solo gli ultimi 7 giorni di misurazioni e calcolare la media ponderata
def modifyed_data(data):
    translater= Translator()
    for metric in data['metrics']:
        valid_points=[dp for dp in metric['data_points'] if dp['sample_size']>0 and dp['sample_size'] is not None ]
            
        valid_points = valid_points[-7:]
        n_sample_size=0
        n_zero_sample_size=0
        weighted_average=0
        metric['type']= translater.translate(metric['type'], dest='it').text
        if len(valid_points)<7 :
            metric['weithted_average']= 'Non sufficienti elementi per calcolarla'
        else:
            for data_point in valid_points:
                if data_point['sample_size']:
                    weighted_average += data_point['average'] * data_point['sample_size']
                    n_sample_size += data_point['sample_size']
                else:
                    n_zero_sample_size +=1
            metric['weighted_average']= weighted_average / n_sample_size if n_sample_size!=0 else 0
            metric['n_zero_sample_size']= n_zero_sample_size
       
    return data