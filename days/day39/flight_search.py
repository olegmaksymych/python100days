import requests
import os
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
	"""Handles flight search using the Amadeus API."""

	def __init__(self):
		"""Initialize with API credentials and fetch authentication token."""
		self._api_key = os.environ.get("API_KEY")
		self._api_secret = os.environ.get("AMADEUS_API_SECRET")
		self._base_url = "https://test.api.amadeus.com"  # Test environment URL
		self._token = self._get_new_token()

	def _get_new_token(self):
		"""Fetch a new access token from Amadeus."""
		url = f"{self._base_url}/v1/security/oauth2/token"
		headers = {"Content-Type": "application/x-www-form-urlencoded"}
		data = {
			"grant_type": "client_credentials",
			"client_id": self._api_key,
			"client_secret": self._api_secret
		}

		response = requests.post(url, headers=headers, data=data)
		response.raise_for_status()  # Raise an error for bad responses

		token_data = response.json()
		return token_data["access_token"]  # Return the token

	def get_iata_code(self, city_name):
		"""Fetch real IATA code for a given city."""
		print(f"Fetching IATA Code for {city_name}...")

		url = f"{self._base_url}/v1/reference-data/locations"
		headers = {
			"Authorization": f"Bearer {self._token}",
			"Content-Type": "application/json"
		}
		params = {
			"subType": "CITY",
			"keyword": city_name
		}

		response = requests.get(url, headers=headers, params=params)

		if response.status_code == 200:
			data = response.json()
			if data["data"]:
				return data["data"][0]["iataCode"]  # Return the IATA code
			else:
				return "Not Found"
		else:
			print(f"Error: {response.json()}")
			return None

	def search_flights(self, origin_iata, destination_iata, departure_date, return_date=None):
		"""
		Search for flights using the Amadeus API.
		:param origin_iata: IATA code of departure city.
		:param destination_iata: IATA code of destination city.
		:param departure_date: Date of departure (YYYY-MM-DD).
		:param return_date: Optional return date for round trips.
		:return: JSON response with flight details.
		"""
		url = f"{self._base_url}/v2/shopping/flight-offers"
		headers = {
			"Authorization": f"Bearer {self._token}",
			"Content-Type": "application/json"
		}
		params = {
			"originLocationCode": origin_iata,
			"destinationLocationCode": destination_iata,
			"departureDate": departure_date,
			"adults": 1,
			"max": 5  # Limit to 5 results
		}
		if return_date:
			params["returnDate"] = return_date  # Include return date if available

		response = requests.get(url, headers=headers, params=params)
		if response.status_code == 200:
			return response.json()  # Return flight data
		else:
			print(f"Flight Search Error: {response.json()}")
			return None
