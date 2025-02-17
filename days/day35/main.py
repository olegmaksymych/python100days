from twilio.rest import Client
import requests
from datetime import datetime
API_KEY = "should find in the appropriate account"
ACCOUNT_SID = "should find in the appropriate account"
AUTH_TOKEN = "should find in the appropriate account"



# https://api.openweathermap.org/data/2.5/weather?q=Lviv,UA&appid=fdb71bc53d6bd99bdbeff309f23ae14f
main_link = "http://api.openweathermap.org/data/2.5/forecast"
lat = 46.482525
lon = 30.723309
weather_params = {
	"lat": lat,
	"lon": lon,
	"appid": API_KEY,
	"cnt": 4
}

response = requests.get(main_link, params=weather_params)
print(response.raise_for_status())
weather_params = response.json()
print(weather_params)

# Iterate through the list (forecast entries)
will_rain = False
for hour in weather_params["list"]:
	date_obj = datetime.strptime(hour["dt_txt"] , "%Y-%m-%d %H:%M:%S")
	formatted_date = date_obj.strftime("%A %H:%M o'clock")
	for weather_entry in hour["weather"]:  # "weather" is a list
		if weather_entry["id"] < 700:
			will_rain = True
if will_rain:
	sender = Client(ACCOUNT_SID, AUTH_TOKEN)

	message = sender.messages.create(
		from_='+18149047562',
		body="Do not forget an umbrella",
		to='+380991554093'
	)
	print(message.sid)
