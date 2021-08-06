import requests
import csv
import string
import numpy as np 
import pandas as pd

import time
import json
from requests import api
import ast


sheet_id = "1_Rxr-2jkJgWmmO6xLJJ61SHEXeRCUVIgv6cXXnvz438"
sheet_name = "Cities".replace(" ", "%20")
cities_states_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"


df = pd.read_csv(cities_states_url, header = 0)

def get_key():

    with open("/home/richarda/apikeys/open_weather_api_key","r") as file_object:
        api_key = file_object.readline().strip()

    return api_key


def weather_conditions_codes():
#one way I thought about getting the weather conditions thought the api query
    weather_conditions = {
    'Thunderstorm': ["200", "201", "202", "210", "211", "212", "221", "230", "231", "232"], 
    'Drizzle':["300", "301", "302", "310", "311", "312", "313", "314", "321"], 
    'Rain': ["500", "501", "502", "503", "504", "511","520", "521", "522", "531"], 
    'Snow': ["600", "601", "602", "611", "612", "613", "615", "616", "620", "621", "622"], 
    'Atmosphere': ["701", "711", "721", "731", "741", "751", "761", "762", "771", "781"], 
    'Clear': ["800"], 
    'Clouds':["801", "802", "803", "804"]
    }

    return weather_conditions

# print(get_weather_conditions())

def get_cities():

    cities = []

    for i, city in df.iterrows():
        cities.append(city[0])

    return cities

def get_states():
#tried using this to filter api query but filtering by state didn't work. 
    states = []

    for i, state in df.iterrows():
        states.append(state[1])

    return states

def get_weather_info():
    #save this to json tomorrow
    cities = get_cities()
    states = get_states()

    api_key = get_key()
    country_code = "US"

    weather_data = {}

    # if " " in state_code:
    #     state_code.replace(" ", "%20")
    for i, city in enumerate(cities):
        
        open_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={cities[i]},{states[i]},{country_code}&units=imperial&appid={api_key}"
        time.sleep(3)
        r = requests.get(open_weather_url, stream=True)
        r_data = str(r.content, 'UTF-8')
        print(i,r_data)
        city_state = f"{cities[i]},{states[i]}"
        if city_state not in weather_data:
            weather_data[city_state] = [r_data]

    # weather_data.decode("utf-8")
    # with open('/home/richarda/Projects/horizon_media_project/backend/weatherdata.json', 'w+') as f_obj:
    #     json.dump(weather_data, f_obj, sort_keys = True,indent=4)
    return weather_data

def json_load_data():
    with open('/home/richarda/Projects/horizon_media_project/backend/weatherdata.json', 'r') as f_obj:
        data = json.load(f_obj)

    return data


def post_weather_info():

    data = json_load_data()
    condition_data = []
    condition = "Clear" #Drizzle, Rain Snow, Atmosphere, Clear, Clouds, Thunderstorm

    for k, v in data.items():
        res = ast.literal_eval(data[k][0])
        # print(res)
        try:
            if condition == res["weather"][0]["main"]:
                weather_report = res["main"]["temp"], res["wind"]["speed"]
                condition_data.append({k:weather_report})
        except:
            pass

    # return data['West Jordan,Utah'][0], type(data['West Jordan,Utah'][0])
    # return res["weather"][0]["main"]
    return condition_data


# if __name__ == "__main__":
#     app.run(debug=True)