from datetime import datetime, timezone
import requests
import smtplib
import time

# Your coordinates
MY_LAT = 49.8072
MY_LONG = 24.0493

# Email credentials
EMAIL = "THE EMAIL ADDRESS SHOULD BE@gmail.com"
PASSWORD = "HERE SHOULD BE THE PASSWORD FOR EMAIL"


def is_iss_overhead():
    """Check if the ISS is within the proximity range of your location."""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])
    return (
            MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and
            MY_LONG - 5 <= iss_long <= MY_LONG + 5
    )


def is_night():
    """Check if it's currently dark at the user's location."""
    params = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=params, verify=True)  # Fix SSL warning
    # response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(':')[0])

    time_now = datetime.now(timezone.utc).hour  # Fix DeprecationWarning
    return time_now >= sunset or time_now <= sunrise  # Returns True if it's dark


def send_notification_email():
    """Send an email notification when the ISS is overhead and it's dark."""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="olehmaksymych@icloud.com",
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky!"
        )
        print("Email sent!")


# Run the check every 60 minutes
while True:
    time.sleep(60)  # Wait 1 minute (60 seconds)
    if is_night() and is_iss_overhead():
        send_notification_email()

