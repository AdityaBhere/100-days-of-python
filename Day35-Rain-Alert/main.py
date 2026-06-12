import requests
import os

api_key = os.environ["API_KEY"]
url = "http://api.openweathermap.org/data/2.5/forecast"
parameter = {
    "lat": 19.878931,
    "lon": 75.363252,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url, params=parameter)
response.raise_for_status()
weather_data = response.json()

weather_code_list = []
going_to_rain = False

for i in range(4):
    weather_code = weather_data["list"][i]["weather"][0]["id"]
    weather_code_list.append(int(weather_code))

for code in weather_code_list:
    if code < 700:
        going_to_rain = True

if going_to_rain:
    print("Bring an umbrella")