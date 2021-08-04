import requests
import csv
import string
import numpy as np 
import pandas as pd

import time

from requests import api


sheet_id = "1_Rxr-2jkJgWmmO6xLJJ61SHEXeRCUVIgv6cXXnvz438"
sheet_name = "Cities".replace(" ", "%20")
cities_states_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"


df = pd.read_csv(cities_states_url, header = 0)

def get_key():

    with open("/home/richarda/apikeys/open_weather_api_key","r") as file_object:
        api_key = file_object.readline().strip()

    return api_key


def get_weather_conditions():

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

    states = []

    for i, state in df.iterrows():
        states.append(state[1])

    return states

def get_weather_info():

    time.sleep(5)

    api_key = get_key()
    country_code = "us"
    state_code = ""
    city_name = ""

    if " " in state_code:
        state_code.replace(" ", "%20") 
    open_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&units=imperial&appid={api_key}"

    r = requests.get(open_weather_url)
    
    return r.content



if __name__ == "__main__":
    app.run(debug=True)