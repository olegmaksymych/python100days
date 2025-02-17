import requests
from datetime import datetime, timedelta
import json
import os
from dotenv import load_dotenv
load_dotenv()

# API credentials
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("AMADEUS_API_SECRET")
base_url = "https://test.api.amadeus.com"


# 1. Function to get access token
def get_access_token():
    url = f"{base_url}/v1/security/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": api_key,
        "client_secret": api_secret
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    token_data = response.json()
    return token_data["access_token"]


# 2. Function to search for flights
def search_flights(destination_iata):
    """Search for the cheapest direct round-trip flights from LON to a destination."""
    url = f"{base_url}/v2/shopping/flight-offers"
    departure_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    return_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    params = {
        "originLocationCode": "LON",
        "destinationLocationCode": destination_iata,
        "departureDate": departure_date,
        "returnDate": return_date,
        "adults": 1,
        "currencyCode": "GBP",
        "max": 5,
    }
    access_token = get_access_token()  # Get the access token
    headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        with open("token_data.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"Error {response.status_code}: {response.text}")


# 3. Call function with a valid IATA code
search_flights("JFK")  # New York JFK Airport
