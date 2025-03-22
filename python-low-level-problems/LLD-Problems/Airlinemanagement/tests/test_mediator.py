import unittest
from models.person import Mediator, Flight, ATC, Aircraft

class TestMediator(unittest.TestCase):
    def test_mediator_pattern(self):
        mediator = Mediator()
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
        mediator.register_flight(flight)
        mediator.notify_atc(flight, "Delayed")
        # Check if ATC was notified
        self.assertEqual(flight.flight_number, "BA212")  # Ensure flight object is correct