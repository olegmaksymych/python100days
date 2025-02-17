import os

import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# 📊 Sheety API URL (Replace with your own)
SHEETY_ENDPOINT = "https://api.sheety.co/5b3211ad8c70b00bd4c760a96d533388/workoutTracking/workouts"

# Sheety API authentication (If required)
SHEETY_HEADERS = {
    "Authorization": SHEETY_TOKEN,  # If authentication is required
    "Content-Type": "application/json"
}

# Nutritionix API headers
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# 📝 User input (exercise description)
exercise_text = input("Enter your workout (e.g., '30 min yoga'): ")

# 📩 Data for Nutritionix API
user_params = {
    "query": exercise_text,
    "gender": "male",  # Update as needed
    "weight_kg": 71,   # Update as needed
    "height_cm": 171,  # Update as needed
    "age": 30          # Update as needed
}

# 🏋️ Step 1: Get Calories Burned from Nutritionix
response = requests.post(url=NUTRITION_ENDPOINT, json=user_params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
    if "exercises" in data and len(data["exercises"]) > 0:
        exercise = data["exercises"][0]  # Get first result
        exercise_name = exercise["name"].title()
        duration = exercise["duration_min"]
        calories_burned = exercise["nf_calories"]

        print(f"✅ Workout: {exercise_name}, {duration} min, {calories_burned} kcal")

        # 📌 Step 2: Add Data to Google Sheet via Sheety API
        today = datetime.now().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
        now_time = datetime.now().strftime("%H:%M:%S")  # Format: HH:MM:SS

        sheet_data = {
            "workout": {
                "date": today,
                "time": now_time,
                "exercise": exercise_name,
                "duration": duration,
                "calories": calories_burned
            }
        }

        # Send POST request to Sheety
        sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_data, headers=SHEETY_HEADERS)

        if sheety_response.status_code == 200:
            print("✅ Data added to Google Sheet successfully!")
        else:
            print(f"❌ Error adding to Google Sheet: {sheety_response.text}")

    else:
        print("❌ No exercise data found.")
else:
    print(f"❌ Nutritionix API error: {response.status_code}, {response.text}")
