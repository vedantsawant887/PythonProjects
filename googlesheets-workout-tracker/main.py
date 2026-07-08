import requests
import datetime
import os

APP_ID = f"{os.environ.get("APP_ID")}"
API_KEY = f"{os.environ.get("API_KEY")}"


GENDER = "male"
WEIGHT = 55
HEIGHT = 175
AGE = 18

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

api_endpoint = "https://app.100daysofpython.dev"

stats_endpoint = f"{api_endpoint}/v1/nutrition/natural/exercise"

stats_config = {
    "query": input("Tell me what you did? "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER,
}

response = requests.post(stats_endpoint, headers=headers, json=stats_config)
print(response.json())
exercise = response.json()["exercises"][0]["name"]
duration = response.json()["exercises"][0]["duration_min"]
calories = response.json()["exercises"][0]["nf_calories"]


today = datetime.date.today().strftime("%d/%m/%Y")
time = datetime.datetime.now().time().strftime("%H:%M:%S")


sheety_endpoint = f"{os.environ.get("SHEETY_ENDPOINT")}"
sheety_params = {
    "workout":{
        "date":f"{today}",
        "time":f"{time}",
        "exercise":f"{exercise.title()}",
        "calories":f"{calories}",
        "duration":f"{duration}",
    }
}

headers = {"Authorization": f"Bearer {os.environ.get("TOKEN")}"}

response1 = requests.post(sheety_endpoint, headers=headers, json=sheety_params)
print(response1.json())