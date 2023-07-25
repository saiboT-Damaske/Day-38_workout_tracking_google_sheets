import requests
import datetime as dt

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

NUTRI_API_ID = ""
NUTRI_API_KEY = ""

AGE = None
HEIGHT_CM = None
WEIGHT_KG = None
GENDER = "male"

SHEETY_API_ENDPOINT = ""
SHEETY_AUTHORIZATION = ""

# --------------- get workout data-------------- #

# query = input("What exercises did you do today? ")
query = "10km running"

nutri_headers = {
    "x-app-id": NUTRI_API_ID,
    "x-app-key": NUTRI_API_KEY,
}

nutri_body = {
    "query": query,
    "age": AGE,
    "gender": GENDER,
    "height_cm": HEIGHT_CM,
    "weight_kg": WEIGHT_KG,
}


response = requests.post(url=EXERCISE_ENDPOINT, headers=nutri_headers, json=nutri_body)
response.raise_for_status()
print(response.json()["exercises"])
exercise = response.json()["exercises"][0]["user_input"]
duration = response.json()["exercises"][0]["duration_min"]
calories = response.json()["exercises"][0]["nf_calories"]

# --------------- post to sheety -------------- #

sheety_header = {
    "Authorization": SHEETY_AUTHORIZATION
}


now = dt.datetime.now()
time = now.strftime("%H:%M:%S")
date = now.strftime("%Y-%m-%d")
print(date, time)

sheety_body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,

    }
}

response = requests.post(url=SHEETY_API_ENDPOINT, json=sheety_body, headers=sheety_header)
response.raise_for_status()
print(response.json())

response = requests.get(url=SHEETY_API_ENDPOINT, headers=sheety_header)
response.raise_for_status()
print(response.json())
