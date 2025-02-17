import requests
import os
from dotenv import load_dotenv
load_dotenv()

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co/5b3211ad8c70b00bd4c760a96d533388/flightDeals/prices"
SHEETY_HEADERS = {
    "Authorization": SHEETY_TOKEN,
    "Content-Type": "application/json"
}


class DataManager:
    """Handles communication with Google Sheets via Sheety API."""
    def get_data(self):
        """Fetch data from Google Sheets."""
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        print(data["prices"])
        return data["prices"]  # Adjust if necessary based on your sheet structure

    def update_iata_code(self, row_id, new_iata_code):
        """Update a specific row's IATA code in Google Sheets."""
        update_url = f"{SHEETY_ENDPOINT}/{row_id}"
        update_data = {
            "price": {  # "price" must match your Sheety sheet's object name
                "iataCode": new_iata_code
            }
        }
        response = requests.put(url=update_url, json=update_data, headers=SHEETY_HEADERS)
        return response.json()

    def get_prices_dict(self):
        """Returns a dictionary of IATA codes and their current prices."""
        data = self.get_data()
        return {entry["iataCode"]: entry["lowestPrice"] for entry in data}