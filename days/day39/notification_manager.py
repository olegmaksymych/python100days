import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

EMAIL = os.environ.get("SENDER")
PASSWORD = os.environ.get("PASSWORD")

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_notification_email(self,  price, departure_iata, city, arrival_iata, outbound_date, inbound_date):
        subject = "🔥 Flight Deal Alert!"
        body = (f"Low Price Alert! 🚀\n\n"
                f"Only {price} GBP to fly from London -{departure_iata} to {city} =  {arrival_iata}.\n"
                f"Departure: {outbound_date}\n"
                f"Return: {inbound_date if inbound_date != 'N/A' else 'One-way trip'}\n\n"
                f"Book now before prices go up!")

        message = f"Subject: {subject}\n\n{body}"

        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs="olehmaksymych@icloud.com",
                    msg=message.encode("utf-8")  # Ensure proper encoding
                )
            print(f"✅ Email sent successfully to olehmaksymych@icloud.com!")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")