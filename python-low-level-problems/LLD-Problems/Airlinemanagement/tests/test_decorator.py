import unittest
from models.person import Booking, ExtraBaggageDecorator, InFlightMealDecorator, Passenger, Flight, Aircraft

class TestDecorator(unittest.TestCase):
    def test_extra_baggage_decorator(self):
        passenger = Passenger(1, "John Doe", "john.doe@example.com", "123-456-7890")
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
        booking = Booking(1, flight, passenger, "12A", 200)
        booking = ExtraBaggageDecorator(booking)
        self.assertEqual(booking.get_price(), 250)  # $200 + $50 for extra baggage

    def test_in_flight_meal_decorator(self):
        passenger = Passenger(1, "John Doe", "john.doe@example.com", "123-456-7890")
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
        booking = Booking(1, flight, passenger, "12A", 200)
        booking = InFlightMealDecorator(booking)
        self.assertEqual(booking.get_price(), 220)  # $200 + $20 for in-flight meal

    def test_combined_decorators(self):
        passenger = Passenger(1, "John Doe", "john.doe@example.com", "123-456-7890")
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
        booking = Booking(1, flight, passenger, "12A", 200)
        booking = ExtraBaggageDecorator(booking)
        booking = InFlightMealDecorator(booking)
        self.assertEqual(booking.get_price(), 270)  # $200 + $50 + $20