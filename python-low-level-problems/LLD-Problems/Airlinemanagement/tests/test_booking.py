import unittest
from models.person import Booking, BookingFactory, Passenger, Flight, Aircraft

class TestBooking(unittest.TestCase):
    def test_booking_creation(self):
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
        self.assertEqual(booking.booking_id, 1)
        self.assertEqual(booking.passenger.name, "John Doe")
        self.assertEqual(booking.seat, "12A")
        self.assertEqual(booking.price, 200)

    def test_booking_factory(self):
        factory = BookingFactory()
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
        booking = factory.create_booking(1, flight, passenger, "12A", 200)
        self.assertEqual(booking.booking_id, 1)
        self.assertEqual(booking.passenger.name, "John Doe")
        self.assertEqual(booking.seat, "12A")
        self.assertEqual(booking.price, 200)