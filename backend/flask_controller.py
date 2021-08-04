from flask import Flask, request, redirect, session, jsonify, flash, url_for
import requests
from datetime import datetime
import time

#modules
from flask_cors import CORS


#functions
# from util import get_stations
# from util import get_stop_id
# from util import get_weather_conditions
# from util import get_weather_key
# from mta import get_train_time
# from util import all_stations

from util import get_states, get_weather_conditions
from util import get_cities
from util import get_weather_info

app = Flask(__name__)
CORS(app)

#------------------------------------------weather conditions
# @app.route('/train/<letter>', methods =["POST", "GET"])
# @app.route('/weather/<weather_condition>', methods =["POST", "GET"])
# def get_weather_conditions(weather):

#     if request.method == "POST":
#         all_conditions = get_weather_conditions().keys()

#     if request.method == "GET":
#         return ({"conditions": all_conditions})
#     return ({"conditions": all_conditions})

@app.route('/weatherlist')
def get_weather_list():
    weather_conditions = get_weather_conditions().keys()

    condition_list = [k for k in weather_conditions]

    return condition_list


@app.route('/weatherinfo')
def get_weather_data():
    data = get_weather_info()

    return data
    



if __name__ == "__main__":
    app.run(debug=True, port = 5000)