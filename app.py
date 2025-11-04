from  flask import Flask, jsonify
import requests


BASE_URL='https://api.zeroc.green/v1/'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    response= requests.get(BASE_URL + 'stations/')
    
    return response.json()
    
