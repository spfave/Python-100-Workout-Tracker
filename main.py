import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# Constants
NUTRITION_ID = os.getenv("NUTRITION_ID")
NUTRITION_KEY = os.getenv("NUTRITION_KEY")

GENDER = "male"
WEIGHT_KG = 59
HEIGHT_CM = 180
AGE = 31


# Main
exercise_input = input("What did you do for exercise today? ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
headers = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_KEY,
}

response = requests.post(url=exercise_endpoint,json=exercise_params, headers=headers)
exercise_data = response.json()["exercises"]
# print(exercise_data)

date_time = datetime.now()
date_format = date_time.strftime("%m/%d/%Y")
time_format = date_time.strftime("%X")


workout_spreadsheet_username = os.getenv("SHEETLY_USERNAME")
workout_spreadsheet_project_name = "workoutTracker"
workout_spreadsheet_sheet_name = "workouts"
workout_spreadsheet_endpoint = f"https://api.sheety.co/{workout_spreadsheet_username}/{workout_spreadsheet_project_name}/{workout_spreadsheet_sheet_name}"
workout_spreadsheet_auth = (os.getenv("AUTH_USERNAME"), os.getenv("AUTH_PASS"))

for exercise in exercise_data:

    exercise_params = {
        "workout": {
            "date": date_format,
            "time": time_format,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=workout_spreadsheet_endpoint, json=exercise_params, auth=workout_spreadsheet_auth)
    print(sheet_response)
