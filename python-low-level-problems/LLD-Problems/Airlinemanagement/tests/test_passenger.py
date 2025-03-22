import unittest
from models.person import Passenger, PassengerFactory

class TestPassenger(unittest.TestCase):
    def test_passenger_creation(self):
        passenger = Passenger(1, "John Doe", "john.doe@example.com", "123-456-7890")
        self.assertEqual(passenger.name, "John Doe")
        self.assertEqual(passenger.email, "john.doe@example.com")
        self.assertEqual(passenger.phone, "123-456-7890")

    def test_passenger_factory(self):
        factory = PassengerFactory()
        passenger = factory.create_passenger(1, "Jane Doe", "jane.doe@example.com", "987-654-3210")
        self.assertEqual(passenger.name, "Jane Doe")
        self.assertEqual(passenger.email, "jane.doe@example.com")
        self.assertEqual(passenger.phone, "987-654-3210")