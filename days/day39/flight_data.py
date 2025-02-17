from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta


class FlightData:
    """Handles flight data comparison and notifications."""

    def __init__(self):
        """Initialize FlightData with necessary components."""
        self.flight_search = FlightSearch()  # Use FlightSearch for API calls
        self.data_manager = DataManager()  # Manage Google Sheet data
        self.notification_manager = NotificationManager()  # Send notifications
        self.prices_dict = self.data_manager.get_prices_dict()  # Get stored prices

    def find_deals(self, departure_iata, days_ahead=30):
        """
        Check for cheaper flights and notify if a deal is found.
        :param departure_iata: IATA code of the departure airport.
        :param days_ahead: Number of days in the future to search flights.
        """
        departure_date = (datetime.today() + timedelta(days=days_ahead)).strftime("%Y-%m-%d")

        for city, sheet_price in self.prices_dict.items():
            destination_iata = self.flight_search.get_iata_code(city)
            if not destination_iata:
                print(f"Skipping {city} - IATA code not found.")
                continue

            # FIX: Pass all required arguments
            flight_data = self.flight_search.search_flights(departure_iata, destination_iata, departure_date)

            if flight_data and "data" in flight_data:
                for flight in flight_data["data"]:
                    price = float(flight["price"]["total"])
                    outbound_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                    inbound_date = (flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                                    if len(flight["itineraries"]) > 1 else "N/A")
                    departure_iata = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                    arrival_iata = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]

                    if price < sheet_price:
                        print(f"✅ Deal found: {arrival_iata} for {price} GBP (Old: {sheet_price} GBP)")

                        # Send an email notification
                        self.notification_manager.send_notification_email(price, departure_iata, city, arrival_iata, outbound_date, inbound_date)