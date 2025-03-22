import unittest
from models.person import FlightManager, Flight, Aircraft

class TestFlightManager(unittest.TestCase):
    def test_create_flight_template(self):
        flight_manager = FlightManager()
        aircraft = Aircraft(1, "Boeing 737", 150)
        flight = flight_manager.create_flight_template(
            src="London",
            dest="Tokyo",
            scheduled_departure="10:00",
            scheduled_arrival="18:00",
            operating_days=["Monday", "Friday"],
            aircraft=aircraft,
            price_per_seat=200,
            bag_allowance=20,
            extra_baggage_fee=10
        )
        self.assertEqual(flight.flight_number, "FL1")
        self.assertEqual(flight.source, "London")
        self.assertEqual(flight.destination, "Tokyo")