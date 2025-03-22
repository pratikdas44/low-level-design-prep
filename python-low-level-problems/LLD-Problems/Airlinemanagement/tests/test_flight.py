import unittest
from models.person import Flight, Aircraft
from models.enums import FlightStatus

class TestFlight(unittest.TestCase):
    def test_flight_creation(self):
        aircraft = Aircraft(1, "Boeing 737", 150)
        flight = Flight(
            flight_number="BA212",
            source="London",
            destination="Tokyo",
            scheduled_departure="10:00",
            scheduled_arrival="18:00",
            operating_days=["Monday", "Friday"],
            aircraft=aircraft,
            price_per_seat=200,
            bag_allowance=20,
            extra_baggage_fee=10
        )
        self.assertEqual(flight.flight_number, "BA212")
        self.assertEqual(flight.source, "London")
        self.assertEqual(flight.destination, "Tokyo")
        self.assertEqual(flight.flight_status, FlightStatus.SCHEDULED)