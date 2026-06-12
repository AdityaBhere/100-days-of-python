import requests
from datetime import datetime
import os


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key":API_KEY
}

base_url = "https://app.100daysofpython.dev"

exercise = input("Tell me what you did?: ")

calorie_query = {
  "query": exercise,
  "weight_kg": 60,
  "height_cm": 170,
  "age": 19,
  "gender": "male"
}

calorie_query_url = f"{base_url}/v1/nutrition/natural/exercise"
calorie_response = requests.post(url=calorie_query_url, json=calorie_query, headers=headers).json()


workout_base_url = f"https://api.sheety.co/{os.environ["SHEET_ENDPOINT"]}"
headers = {
    "Authorization": f"Basic {os.environ["AUTH_KEY"]}"
}

for workout in calorie_response["exercises"]:
    workout_request = {
        "sheet1": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }
    response = requests.post(url=workout_base_url, json=workout_request, headers=headers)
    print(response.text)


