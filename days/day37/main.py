from datetime import datetime
import requests
USERNAME = "olehmaksymych"
TOKEN = "desrbjgdlbmsfes"
GRAPH_ID = "graph1"
today_date = datetime.today().strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
	"token": TOKEN,
	"username":	USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
	"id": GRAPH_ID,
	"name": "The Cycling Graph",
	"unit": "Km",
	"type": "float",
	"color": "sora",
}

headers = {
	"X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
	"date": today_date,
	"quantity": input("How many kilometers did you cycle?"),
}
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)



update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"


new_pixel_data = {
	"quantity": "4.5"
}


response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)