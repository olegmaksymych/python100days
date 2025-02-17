import requests

parameters = {
    "amount": 20,
    "type": "boolean",
    "category": 18
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # Ensures that any HTTP error raises an exception

data = response.json()  # Convert response to JSON format
question_data = (data["results"])  # Print the actual JSON data
