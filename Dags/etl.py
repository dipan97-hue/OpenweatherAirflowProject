import requests
import json
import pandas as pd
from datetime import datetime
from pprint import pprint

def kelvin_to_celsius(temp):
    return temp - 273.15
def transform_load_data():
        
    api_key = ""  # Replace with your actual API key

    weather_api = f'http://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid={api_key}'
    response = requests.get(weather_api)
    data = response.json()
    city = data['city']['name']
    for forecast in data['list']:

        weather_description = forecast['weather'][0]['description']
    
        temperature = kelvin_to_celsius(forecast['main']['temp'])
        feels_like_temperature = kelvin_to_celsius(forecast['main']['feels_like'])
        max_temperature = kelvin_to_celsius(forecast['main']['temp_max'])
        min_temperature = kelvin_to_celsius(forecast['main']['temp_min'])
        humditity = forecast['main']['humidity']
        pressure = forecast['main']['pressure']
        wind_speed = forecast['wind']['speed']
        wind_direction = forecast['wind']['deg']
        cloudiness = forecast['clouds']['all']
        wind_gust = forecast['wind']['gust']
        visibility = forecast['visibility']
    sunrise = data['city']['sunrise']
    sunrisetime = datetime.fromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S')
    sunset = data['city']['sunset']
    sunsettime = datetime.fromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S')
    transformed_data = { 'city': city,
                        'weather_description': weather_description,
                        'temperature': temperature,
                        'feels_like_temperature(C)': feels_like_temperature,
                        'max_temperature(C)': max_temperature,
                        'min_temperature(C)': min_temperature,
                        'humidity': humditity,
                        'pressure': pressure,
                        'wind_speed': wind_speed,
                        'wind_direction': wind_direction,
                        'cloudiness': cloudiness,
                        'wind_gust': wind_gust,
                        'visibility': visibility,
                        'sunrise(Local Time)': sunrisetime,
                        'sunset(Local Time)': sunsettime}
    df_data=pd.DataFrame(transformed_data, index=[0])
    now = datetime.now()
    df_string = 'weather_data_' + now.strftime('%Y%m%d_%H%M%S') 
    df_data.to_csv(f'{df_string}.csv', index=False)

if __name__ == '__main__':
    transform_load_data()





