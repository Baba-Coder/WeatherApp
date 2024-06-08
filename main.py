import requests
from pprint import pprint

API_Key = '47be0dd3e489572682b5bd931e29b03e'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
