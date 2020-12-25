import os
import requests
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
exercise = input("What did you do for exercise today? ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query": exercise,
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
print(response.json())