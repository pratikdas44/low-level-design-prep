import unittest
from models.person import BookingManager, Passenger, Aircraft, Flight, FlightInstance, Seat

class TestBookingManager(unittest.TestCase):
    def test_create_booking(self):
        booking_manager = BookingManager()
        passenger = Passenger(1, "John Doe", "john.doe@example.com", "123-456-7890")

        # Create a valid Flight object
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

        # Create a FlightInstance with the valid Flight object
        flight_instance = FlightInstance(
            flight_instance_id=101,
            flight=flight,  # Pass the Flight object here
            flight_date="2023-10-30",
            available_seats=150,
            flight_status="Scheduled"
        )

        seat = Seat(seat_number="12A", seat_type="Economy")
        booking = booking_manager.create_booking(passenger, flight_instance, seat)
        self.assertEqual(booking.booking_id, 1)
        self.assertEqual(booking.price, 200)