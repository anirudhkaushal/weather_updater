import requests
# import os
from pprint import pprint

def get_weather_forecast():

    request_url = 'https://api.open-meteo.com/v1/forecast?latitude=39.7684&longitude=-86.158&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=America%2FChicago&forecast_days=1'

    # print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)
    # print("\nToday's weather forcast for Indianapolis")
    # print(f'\nDate: {weather_data["daily"]["time"]}')
    # print(f'\nMinimum temperature(in celsius) is {weather_data["daily"]["temperature_2m_min"]}')
    # print(f'\nMaximum temperature(in celsius) is {weather_data["daily"]["temperature_2m_max"]}')

    with open('README.md', 'w') as readme_file:
        readme_file.write(f'# Indianapolis weather forecast \nDate: {weather_data["daily"]["time"]} \n\nMinimum temperature(in celsius) is {weather_data["daily"]["temperature_2m_min"]} \nMaximum temperature(in celsius) is {weather_data["daily"]["temperature_2m_max"]}')


if __name__ == "__main__":
    get_weather_forecast()

