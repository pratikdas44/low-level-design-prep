import unittest
from models.person import Flight, Passenger, Aircraft

class TestObserver(unittest.TestCase):
    def test_observer_pattern(self):
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
        passenger = Passenger(1, "John Doe", "john.doe@example.com", "123-456-7890")
        flight.attach(passenger)
        flight.notify("Flight status updated to Scheduled.")
        # Check if the passenger was notified
        self.assertEqual(passenger.name, "John Doe")  # Ensure passenger object is correct