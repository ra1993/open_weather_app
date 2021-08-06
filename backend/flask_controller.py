from flask import Flask, request, redirect, session, jsonify, flash, url_for
import requests
from datetime import datetime
import time

#modules
from flask_cors import CORS


from util import get_states, get_weather_conditions
from util import get_cities
from util import post_weather_info

app = Flask(__name__)
CORS(app)


@app.route('/weatherlist')
def get_weather_list():
    weather_conditions = get_weather_conditions().keys()

    condition_list = [k for k in weather_conditions]

    return condition_list


@app.route('/weatherinfo')
def post_weather_data():
    data = post_weather_info()

    return data
    



if __name__ == "__main__":
    app.run(debug=True, port = 5000)