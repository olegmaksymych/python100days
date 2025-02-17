import pandas as pd
import smtplib
import random
from datetime import datetime as dt

# Your email credentials
MY_EMAIL = "THE EMAIL ADDRESS SHOULD BE@gmail.com"
MY_PASSWORD = "HERE SHOULD BE THE ACTUAL PASSWORD"

# Load the CSV file into a DataFrame
df = pd.read_csv("birthdays.csv")

# Ensure 'month' and 'day' columns are integers
df["month"] = df["month"].astype(int)
df["day"] = df["day"].astype(int)

# Get today's month and day
current_date = dt.today()
current_month, current_day = current_date.month, current_date.day

# Create a dictionary to store birthdays
birthdays_dict = {}

for _, row in df.iterrows():
	key = (row["month"], row["day"])
	if key not in birthdays_dict:
		birthdays_dict[key] = []
	birthdays_dict[key].append(row.to_dict())

# If today matches a birthday
if (current_month, current_day) in birthdays_dict:
	for birthday_person in birthdays_dict[(current_month, current_day)]:
		name = birthday_person["name"]
		email = birthday_person["email"]

		# Pick a random letter template
		letter_file = f"letter_templates/letter_{random.randint(1, 3)}.txt"

		# Read and personalize the letter
		with open(letter_file, "r") as file:
			letter_content = file.read().replace("[NAME]", name)

		# Send email
		with smtplib.SMTP("smtp.gmail.com") as connection:
			connection.starttls()  # Secure connection
			connection.login(user=MY_EMAIL, password=MY_PASSWORD)
			connection.sendmail(
				from_addr=MY_EMAIL,
				to_addrs=email,
				msg=f"Subject: Happy Birthday!\n\n{letter_content}"
			)
			connection.close()

		print(f"Birthday email sent to {name} at {email} using {letter_file}!")
else:
	print("No birthdays today.")

