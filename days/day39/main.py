from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

# Initialize classes
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
flight_data.find_deals("LON")
# Fetch data from Google Sheet
sheet_data = data_manager.get_data()

# Loop through each row and update missing IATA codes
for row in sheet_data:
    if row["iataCode"] == "":  # If IATA code is missing
        city_name = row["city"]
        new_iata = flight_search.get_iata_code(city_name)  # Get placeholder IATA code

        # Send update request to Sheety
        update_response = data_manager.update_iata_code(row["id"], new_iata)
        print(f"Updated {city_name} with IATA Code: {new_iata}")
        pprint(update_response)  # Optional: Show API response

print("✅ All missing IATA codes have been updated.")
pprint(sheet_data)