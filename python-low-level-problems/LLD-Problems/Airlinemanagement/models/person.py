from datetime import datetime
from typing import Optional
from typing import List
from abc import ABC, abstractmethod
from threading import Lock

class System:
    _instance = None

    def __new__(cls):
        """
        Override the __new__ method to ensure only one instance of the System class is created.
        """
        if cls._instance is None:
            # Create a new instance if it doesn't exist
            cls._instance = super(System, cls).__new__(cls)
            cls._instance.__initialized = False  # Mark as not yet initialized
        return cls._instance  # Return the existing instance

    def __init__(self):
        if not self.__initialized:
            self.passengers = []
            self.flights = []
            self.crew_members = []
            self.aircrafts = []
            self.bookings = []
            self.payments = []
            self.__initialized = True

    def initialize_system(self):
        print("system initialized")

    def get_system_status(self):
        status = {
            "passengers": len(self.passengers),
            "flights": len(self.flights),
            "crew_members": len(self.crew_members),
            "aircrafts": len(self.aircrafts),
            "bookings": len(self.bookings),
            "payments": len(self.payments)
        }
        return status

    def generate_report(self):
        """
        Generate a report summarizing the system's current state.
        """
        status = self.get_system_status()
        report = f"""
        === Airline Management System Report ===
        Passengers: {status['passengers']}
        Flights: {status['flights']}
        Crew Members: {status['crew_members']}
        Aircrafts: {status['aircrafts']}
        Bookings: {status['bookings']}
        Payments: {status['payments']}
        """
        return report

class Passenger:
    def __init__(self, passenger_id, name, email, phone):
        self.passenger_id = passenger_id
        self.name = name
        self.email = email
        self.phone = phone
        self.bookings = []

    def update_details(self, name=None, email=None, phone=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone

    def update(self, message):
        print(f"Passenger {self.name} notified: {message}")

    def get_booking_history(self):
        return self.bookings

    def initiate_payment(self, booking, payment_method):
        return {"booking_id": booking.booking_id, "payment_method": payment_method, "status": "Pending"}

class CrewMember:
    def __init__(self, crew_id, name, email, phone, role, exp_year, license_id):
        self.crew_id = crew_id
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role
        self.exp_year = exp_year
        self.license_id = license_id
        self.assigned_flight_instances = []  # List to store assigned flight instances

    def get_assigned_flight_instances(self):
        return self.assigned_flight_instances

class Flight:
    def __init__(self, flight_number, source, destination, scheduled_departure, scheduled_arrival, operating_days, aircraft, price_per_seat, bag_allowance, extra_baggage_fee):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.scheduled_departure = scheduled_departure
        self.scheduled_arrival = scheduled_arrival
        self.operating_days = operating_days
        self.aircraft = aircraft
        self.price_per_seat = price_per_seat
        self.bag_allowance = bag_allowance
        self.extra_baggage_fee = extra_baggage_fee
        self.flight_status = "Scheduled"  # Add this line
        self.observers = []  # List of observers (passengers)

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def add_operating_day(self, day):
        if day not in self.operating_days:
            self.operating_days.append(day)
            print(f"Added {day} to operating days.")
        else:
            print(f"{day} is already in operating days.")

    def remove_operating_day(self, day):
        if day in self.operating_days:
            self.operating_days.remove(day)
            print(f"Removed {day} from operating days.")
        else:
            print(f"{day} is not in operating days.")

    def get_flight_instances(self, start_date: datetime, end_date: datetime) -> List['FlightInstance']:
        return [instance for instance in self.flight_instances if start_date <= instance.flight_date <= end_date]

    def remove_flight(self):
        print(f"Flight {self.flight_number} has been removed.")

    def get_flight_details(self):
        return {
            "flight_number": self.flight_number,
            "source": self.source,
            "destination": self.destination,
            "scheduled_departure": self.scheduled_departure,
            "scheduled_arrival": self.scheduled_arrival,
            "operating_days": self.operating_days,
            "aircraft": self.aircraft.model,
            "price_per_seat": self.price_per_seat,
            "bag_allowance": self.bag_allowance,
            "extra_baggage_fee": self.extra_baggage_fee
        }



class FlightInstance:
    def __init__(self, flight_instance_id, flight, flight_date, available_seats, flight_status="Scheduled"):
        self.flight_instance_id = flight_instance_id
        self.flight = flight
        self.flight_date = flight_date
        self.available_seats = available_seats
        self.flight_status = flight_status
        self.assigned_crew = []  # List to store assigned crew members
        self.seat_lock = Lock()  # Lock for thread-safe seat operations
        self.status_lock = Lock()  # Lock for thread-safe status updates

    def assign_crew(self, crew_member):
        with self.status_lock:  # Thread-safe block
            self.assigned_crew.append(crew_member)
            print(f"Assigned {crew_member.name} to flight instance {self.flight_instance_id}.")

    def update_status(self, status):
        with self.status_lock:  # Thread-safe block
            self.flight_status = status
            print(f"Updated status of flight instance {self.flight_instance_id} to {status}.")

    def reserve_seat(self):
        """
        Reserve a seat in a thread-safe manner.
        """
        with self.seat_lock:  # Thread-safe block
            if self.available_seats > 0:
                self.available_seats -= 1
                print(f"Seat reserved. Available seats: {self.available_seats}.")
            else:
                raise ValueError("No seats available.")

    def get_available_seats(self):
        with self.seat_lock:  # Thread-safe block
            return self.available_seats

    def calculate_revenue(self):
        total_seats = self.flight.aircraft.total_seats
        return self.flight.price_per_seat * (total_seats - self.available_seats)

    def get_flight_instance_details(self):
        return {
            "flight_instance_id": self.flight_instance_id,
            "flight_number": self.flight.flight_number,
            "flight_date": self.flight_date,
            "available_seats": self.available_seats,
            "flight_status": self.flight_status,
            "assigned_crew": [crew.name for crew in self.assigned_crew]
        }

    def calculate_occupancy(self):
        total_seats = self.flight.aircraft.total_seats
        return ((total_seats - self.available_seats) / total_seats) * 100

class Aircraft:
    def __init__(self, aircraft_id, model, total_seats):
        self.aircraft_id = aircraft_id
        self.model = model
        self.total_seats = total_seats
        self.assigned_flight_instances = []  # List to store assigned flight instances

    def assign_to_flight_instance(self, flight_instance):
        self.assigned_flight_instances.append(flight_instance)
        print(f"Assigned aircraft {self.model} to flight instance {flight_instance.flight_instance_id}.")

    def get_assigned_flight_instances(self):
        return self.assigned_flight_instances

    def get_aircraft_details(self):
        return {
            "aircraft_id": self.aircraft_id,
            "model": self.model,
            "total_seats": self.total_seats,
            "assigned_flight_instances": [instance.flight_instance_id for instance in self.assigned_flight_instances]
        }

    def remove_from_flight_instance(self, flight_instance):
        if flight_instance in self.assigned_flight_instances:
            self.assigned_flight_instances.remove(flight_instance)
            print(f"Removed aircraft {self.model} from flight instance {flight_instance.flight_instance_id}.")
        else:
            print(f"Aircraft {self.model} is not assigned to flight instance {flight_instance.flight_instance_id}.")

class Booking:
    def __init__(self, booking_id, flight_instance, passenger, seat, price, booking_status="Confirmed", cancellation_fee=0, refund_status="None"):
        """
        Initialize a Booking object.
        :param booking_id: Unique ID for the booking.
        :param flight_instance: FlightInstance object associated with the booking.
        :param passenger: Passenger object making the booking.
        :param seat: Seat object assigned to the passenger.
        :param price: Total price of the booking.
        :param booking_status: Status of the booking (e.g., "Confirmed", "Cancelled").
        :param cancellation_fee: Fee for cancelling the booking.
        :param refund_status: Status of the refund (e.g., "None", "Pending", "Processed").
        """
        self.booking_id = booking_id
        self.flight_instance = flight_instance
        self.passenger = passenger
        self.seat = seat
        self.price = price
        self.booking_status = booking_status
        self.cancellation_fee = cancellation_fee
        self.refund_status = refund_status
        self.booking_timestamp = datetime.now()

    def get_price(self):
        """
        Get the price of the booking.
        :return: Price of the booking.
        """
        return self.price

    def cancel_booking(self):
        """
        Cancel the booking and update the booking status and refund status.
        """
        self.booking_status = "Cancelled"
        self.refund_status = "Pending"
        print(f"Booking {self.booking_id} has been cancelled.")

    def calculate_refund(self):
        """
        Calculate the refund amount after deducting the cancellation fee.
        :return: Refund amount.
        """
        return self.price - self.cancellation_fee

    def update_seat(self, new_seat):
        """
        Update the seat assigned to the passenger.
        :param new_seat: New Seat object to assign.
        """
        self.seat = new_seat
        print(f"Seat updated for booking {self.booking_id}.")

    def update_booking_status(self, booking_status):
        """
        Update the status of the booking.
        :param booking_status: New booking status (e.g., "Confirmed", "Cancelled").
        """
        self.booking_status = booking_status
        print(f"Booking status updated to {booking_status} for booking {self.booking_id}.")

    def get_booking_details(self):
        """
        Get details of the booking.
        :return: Dictionary containing booking details.
        """
        return {
            "booking_id": self.booking_id,
            "flight_instance": self.flight_instance.flight_instance_id,
            "passenger": self.passenger.name,
            "seat": self.seat.seat_number,
            "price": self.price,
            "booking_status": self.booking_status,
            "cancellation_fee": self.cancellation_fee,
            "refund_status": self.refund_status,
            "booking_timestamp": self.booking_timestamp
        }

class Seat:
    def __init__(self, seat_number, seat_type, seat_status="Available"):
        """
        Initialize a Seat object.
        :param seat_number: Unique seat number.
        :param seat_type: Type of seat (e.g., "Economy", "Business", "First Class").
        :param seat_status: Status of the seat (e.g., "Available", "Booked").
        """
        self.seat_number = seat_number
        self.seat_type = seat_type
        self.seat_status = seat_status

    def is_available(self):
        """
        Check if the seat is available.
        :return: True if available, False otherwise.
        """
        return self.seat_status == "Available"

    def reserve_seat(self):
        """
        Reserve the seat.
        """
        if self.is_available():
            self.seat_status = "Booked"
            print(f"Seat {self.seat_number} has been reserved.")
        else:
            print(f"Seat {self.seat_number} is already booked.")

    def update_status(self, seat_status):
        """
        Update the status of the seat.
        :param seat_status: New seat status (e.g., "Available", "Booked").
        """
        self.seat_status = seat_status
        print(f"Seat {self.seat_number} status updated to {seat_status}.")

    def get_seat_details(self):
        """
        Get details of the seat.
        :return: Dictionary containing seat details.
        """
        return {
            "seat_number": self.seat_number,
            "seat_type": self.seat_type,
            "seat_status": self.seat_status
        }

    def is_window_seat(self):
        """
        Check if the seat is a window seat.
        :return: True if window seat, False otherwise.
        """
        return self.seat_number.endswith("A") or self.seat_number.endswith("F")

class Payment:
    def __init__(self, payment_id, pay_method, amount, pay_status="Pending", txn_id=None):
        """
        Initialize a Payment object.
        :param payment_id: Unique ID for the payment.
        :param pay_method: Payment method (e.g., "Credit Card", "UPI").
        :param amount: Amount paid.
        :param pay_status: Status of the payment (e.g., "Pending", "Success", "Failed").
        :param txn_id: Transaction ID (optional).
        """
        self.payment_id = payment_id
        self.pay_method = pay_method
        self.amount = amount
        self.pay_status = pay_status
        self.payment_date = datetime.now()
        self.txn_id = txn_id

    def process_payment(self):
        """
        Process the payment.
        """
        self.pay_status = "Success"
        print(f"Payment {self.payment_id} processed successfully.")
        return {
            "status": self.pay_status,
            "method": self.pay_method,
            "amount": self.amount
        }

    def refund_payment(self):
        """
        Refund the payment.
        """
        self.pay_status = "Refunded"
        print(f"Payment {self.payment_id} has been refunded.")

    def get_payment_details(self):
        """
        Get details of the payment.
        :return: Dictionary containing payment details.
        """
        return {
            "payment_id": self.payment_id,
            "pay_method": self.pay_method,
            "amount": self.amount,
            "pay_status": self.pay_status,
            "payment_date": self.payment_date,
            "txn_id": self.txn_id
        }

class BookingManager:
    def __init__(self):
        """
        Initialize the BookingManager with an empty list of bookings.
        """
        self.bookings = []
        self.booking_lock = Lock()

    def create_booking(self, passenger, flight_instance, seat):
        """
        Create a new booking.
        :param passenger: Passenger object making the booking.
        :param flight_instance: FlightInstance object associated with the booking.
        :param seat: Seat object assigned to the passenger.
        :return: Newly created Booking object.
        """
        with self.booking_lock:
            booking_id = len(self.bookings) + 1
            price = flight_instance.flight.price_per_seat
            # Check if the seat is available
            if not seat.is_available():
                raise ValueError(f"Seat {seat.seat_number} is not available.")

            # Reserve the seat
            seat.reserve_seat()
            booking = Booking(booking_id, flight_instance, passenger, seat, price)
            self.bookings.append(booking)
            print(f"Booking {booking_id} created successfully.")
            return booking

    def cancel_booking(self, booking):
        """
        Cancel a booking.
        :param booking: Booking object to cancel.
        """
        with self.booking_lock:
            booking.cancel_booking()
            print(f"Booking {booking.booking_id} has been cancelled.")

    def update_booking(self, booking, new_seat=None, booking_status=None):
        """
        Update a booking in a thread-safe manner.
        :param booking: Booking object to update.
        :param new_seat: New Seat object to assign (optional).
        :param booking_status: New booking status (optional).
        """
        with self.booking_lock:  # Thread-safe block
            if new_seat:
                if not new_seat.is_available():
                    raise ValueError(f"Seat {new_seat.seat_number} is not available.")
                booking.update_seat(new_seat)
            if booking_status:
                booking.update_booking_status(booking_status)
            print(f"Booking {booking.booking_id} updated successfully.")

    def get_booking_details(self, booking):
        """
        Get details of a booking.
        :param booking: Booking object to retrieve details for.
        :return: Dictionary containing booking details.
        """
        return booking.get_booking_details()

    def generate_booking_report(self):
        """
        Generate a report of all bookings.
        :return: List of booking details.
        """
        return [booking.get_booking_details() for booking in self.bookings]

    def get_all_bookings(self):
        """
        Get all bookings.
        :return: List of Booking objects.
        """
        return self.bookings

class PaymentProcessor:
    def __init__(self):
        """
        Initialize the PaymentProcessor with an empty list of payments.
        """
        self.payments = []
        self.payment_lock = Lock()  # Lock for thread-safe payment operations

    def process_payment(self, payment):
        """
        Process a payment.
        :param payment: Payment object to process.
        """
        with self.payment_lock:  # Thread-safe block
            payment.process_payment()
            self.payments.append(payment)
            print(f"Payment {payment.payment_id} processed successfully.")

    def refund_payment(self, payment):
        """
        Refund a payment.
        :param payment: Payment object to refund.
        """
        with self.payment_lock:  # Thread-safe block
            payment.refund_payment()
            print(f"Payment {payment.payment_id} refunded successfully.")

    def validate_payment(self, payment):
        """
        Validate a payment.
        :param payment: Payment object to validate.
        :return: True if payment is valid, False otherwise.
        """
        if payment.amount > 0 and payment.pay_method in ["Credit Card", "UPI", "PayPal"]:
            print(f"Payment {payment.payment_id} is valid.")
            return True
        else:
            print(f"Payment {payment.payment_id} is invalid.")
            return False

    def get_all_payments(self):
        """
        Get all payments.
        :return: List of Payment objects.
        """
        return self.payments

    def generate_payment_report(self):
        """
        Generate a report of all payments.
        :return: List of payment details.
        """
        return [payment.get_payment_details() for payment in self.payments]

class FlightManager:
    def __init__(self):
        """
        Initialize the FlightManager with empty lists for flights and flight instances, and locks for thread-safe operations.
        """
        self.flights = []  # List to store flight templates
        self.flight_instances = []  # List to store flight instances
        self.flight_lock = Lock()  # Lock for thread-safe flight operations
        self.instance_lock = Lock()  # Lock for thread-safe flight instance operations

    def create_flight_template(self, src, dest, scheduled_departure, scheduled_arrival, operating_days, aircraft, price_per_seat, bag_allowance, extra_baggage_fee):
        """
        Create a new flight template in a thread-safe manner.
        :param src: Source airport.
        :param dest: Destination airport.
        :param scheduled_departure: Scheduled departure time.
        :param scheduled_arrival: Scheduled arrival time.
        :param operating_days: List of operating days.
        :param aircraft: Aircraft assigned to the flight.
        :param price_per_seat: Price per seat.
        :param bag_allowance: Baggage allowance in kilograms.
        :param extra_baggage_fee: Extra baggage fee per kilogram.
        :return: Newly created Flight object.
        """
        with self.flight_lock:  # Thread-safe block
            flight_number = f"FL{len(self.flights) + 1}"  # Generate a unique flight number
            flight = Flight(
                flight_number=flight_number,
                source=src,
                destination=dest,
                scheduled_departure=scheduled_departure,
                scheduled_arrival=scheduled_arrival,
                operating_days=operating_days,
                aircraft=aircraft,
                price_per_seat=price_per_seat,
                bag_allowance=bag_allowance,
                extra_baggage_fee=extra_baggage_fee
            )
            self.flights.append(flight)
            print(f"Flight template {flight_number} created successfully.")
            return flight

    def create_flight_instance(self, flight, flight_date, available_seats, flight_status="Scheduled"):
        """
        Create a new flight instance in a thread-safe manner.
        :param flight: Flight template associated with the instance.
        :param flight_date: Date of the flight instance.
        :param available_seats: Number of available seats.
        :param flight_status: Status of the flight instance.
        :return: Newly created FlightInstance object.
        """
        with self.instance_lock:  # Thread-safe block
            flight_instance_id = f"FI{len(self.flight_instances) + 1}"  # Generate a unique flight instance ID
            flight_instance = FlightInstance(
                flight_instance_id=flight_instance_id,
                flight=flight,
                flight_date=flight_date,
                available_seats=available_seats,
                flight_status=flight_status
            )
            self.flight_instances.append(flight_instance)
            print(f"Flight instance {flight_instance_id} created successfully.")
            return flight_instance

    def update_flight_instance_status(self, flight_instance, status):
        """
        Update the status of a flight instance in a thread-safe manner.
        :param flight_instance: FlightInstance object to update.
        :param status: New status (e.g., "Delayed", "Cancelled").
        """
        with self.instance_lock:  # Thread-safe block
            flight_instance.update_status(status)
            print(f"Updated status of flight instance {flight_instance.flight_instance_id} to {status}.")

    def assign_crew_to_flight_instance(self, flight_instance, crew_members):
        """
        Assign crew members to a flight instance in a thread-safe manner.
        :param flight_instance: FlightInstance object to assign crew to.
        :param crew_members: List of CrewMember objects to assign.
        """
        with self.instance_lock:  # Thread-safe block
            for crew_member in crew_members:
                flight_instance.assign_crew(crew_member)
            print(f"Assigned crew to flight instance {flight_instance.flight_instance_id}.")

    def search_flight(self, src, dest, date):
        """
        Search for flight instances based on source, destination, and date.
        :param src: Source airport.
        :param dest: Destination airport.
        :param date: Date of the flight.
        :return: List of matching FlightInstance objects.
        """
        with self.instance_lock:  # Thread-safe block
            return [instance for instance in self.flight_instances
                    if instance.flight.source == src
                    and instance.flight.destination == dest
                    and instance.flight_date == date]

    def get_all_flights(self):
        """
        Get all flight templates.
        :return: List of Flight objects.
        """
        with self.flight_lock:  # Thread-safe block
            return self.flights

    def get_all_flight_instances(self):
        """
        Get all flight instances.
        :return: List of FlightInstance objects.
        """
        with self.instance_lock:  # Thread-safe block
            return self.flight_instances

class FlightSearch:
    def __init__(self, flight_manager: FlightManager):
        """
        Initialize the FlightSearch with a reference to the FlightManager and a lock for thread-safe operations.
        """
        self.flight_manager = flight_manager
        self.search_lock = Lock()  # Lock for thread-safe search operations

    def search_by_route(self, src, dest):
        """
        Search for flight instances based on source and destination in a thread-safe manner.
        :param src: Source airport.
        :param dest: Destination airport.
        :return: List of matching FlightInstance objects.
        """
        with self.search_lock:  # Thread-safe block
            return [instance for instance in self.flight_manager.get_all_flight_instances()
                    if instance.flight.source == src
                    and instance.flight.destination == dest]

    def search_by_date(self, date):
        """
        Search for flight instances based on date in a thread-safe manner.
        :param date: Date of the flight.
        :return: List of matching FlightInstance objects.
        """
        with self.search_lock:  # Thread-safe block
            return [instance for instance in self.flight_manager.get_all_flight_instances()
                    if instance.flight_date == date]

class Baggage:
    def __init__(self, baggage_id, weight, status="Checked-In", extra_fee=0):
        """
        Initialize a Baggage object with a lock for thread-safe operations.
        """
        self.baggage_id = baggage_id
        self.weight = weight
        self.status = status
        self.extra_fee = extra_fee
        self.status_lock = Lock()  # Lock for thread-safe status updates

    def calculate_extra_fee(self, base_allowance):
        """
        Calculate the extra baggage fee in a thread-safe manner.
        :param base_allowance: Base baggage allowance in kilograms.
        :return: Extra baggage fee.
        """
        with self.status_lock:  # Thread-safe block
            if self.weight > base_allowance:
                self.extra_fee = (self.weight - base_allowance) * 10  # $10 per extra kg
            else:
                self.extra_fee = 0
            return self.extra_fee

    def update_status(self, status):
        """
        Update the status of the baggage in a thread-safe manner.
        :param status: New status (e.g., "Checked-In", "In Transit", "Delivered").
        """
        with self.status_lock:  # Thread-safe block
            self.status = status
            print(f"Updated status of baggage {self.baggage_id} to {status}.")

    def get_bag_details(self):
        """
        Get details of the baggage in a thread-safe manner.
        :return: Dictionary containing baggage details.
        """
        with self.status_lock:  # Thread-safe block
            return {
                "baggage_id": self.baggage_id,
                "weight": self.weight,
                "status": self.status,
                "extra_fee": self.extra_fee
            }

    def calculate_total_fee(self, base_allowance):
        """
        Calculate the total baggage fee in a thread-safe manner.
        :param base_allowance: Base baggage allowance in kilograms.
        :return: Total baggage fee.
        """
        with self.status_lock:  # Thread-safe block
            return self.calculate_extra_fee(base_allowance)

class Route:
    def __init__(self, route_id, origin, destination, distance, duration):
        """
        Initialize a Route object with a lock for thread-safe operations.
        """
        self.route_id = route_id
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.duration = duration
        self.route_lock = Lock()  # Lock for thread-safe route updates

    def get_distance(self):
        """
        Get the distance of the route in a thread-safe manner.
        :return: Distance in kilometers.
        """
        with self.route_lock:  # Thread-safe block
            return self.distance

    def get_duration(self):
        """
        Get the duration of the route in a thread-safe manner.
        :return: Duration in hours.
        """
        with self.route_lock:  # Thread-safe block
            return self.duration

    def update_route(self, new_src, new_dest):
        """
        Update the origin and destination of the route in a thread-safe manner.
        :param new_src: New source airport.
        :param new_dest: New destination airport.
        """
        with self.route_lock:  # Thread-safe block
            self.origin = new_src
            self.destination = new_dest
            print(f"Updated route {self.route_id} to {new_src} -> {new_dest}.")

    def get_route_details(self):
        """
        Get details of the route in a thread-safe manner.
        :return: Dictionary containing route details.
        """
        with self.route_lock:  # Thread-safe block
            return {
                "route_id": self.route_id,
                "origin": self.origin,
                "destination": self.destination,
                "distance": self.distance,
                "duration": self.duration
            }

    def calculate_travel_time(self, speed):
        """
        Calculate the travel time based on speed in a thread-safe manner.
        :param speed: Speed in km/h.
        :return: Travel time in hours.
        """
        with self.route_lock:  # Thread-safe block
            return self.distance / speed

class FlightSchedule:
    def __init__(self, schedule_id, route, departure_time, operating_days, assigned_flight_instance):
        """
        Initialize a FlightSchedule object with a lock for thread-safe operations.
        """
        self.schedule_id = schedule_id
        self.route = route
        self.departure_time = departure_time
        self.operating_days = operating_days
        self.assigned_flight_instance = assigned_flight_instance
        self.schedule_lock = Lock()  # Lock for thread-safe schedule updates

    def add_flight_to_schedule(self, flight):
        """
        Add a flight to the schedule in a thread-safe manner.
        :param flight: Flight object to add.
        """
        with self.schedule_lock:  # Thread-safe block
            self.assigned_flight_instance = flight
            print(f"Added flight {flight.flight_number} to schedule {self.schedule_id}.")

    def remove_flight_from_schedule(self, flight):
        """
        Remove a flight from the schedule in a thread-safe manner.
        :param flight: Flight object to remove.
        """
        with self.schedule_lock:  # Thread-safe block
            if self.assigned_flight_instance == flight:
                self.assigned_flight_instance = None
                print(f"Removed flight {flight.flight_number} from schedule {self.schedule_id}.")
            else:
                print(f"Flight {flight.flight_number} is not assigned to schedule {self.schedule_id}.")

    def get_flights_by_day(self, day_of_week):
        """
        Get flights operating on a specific day in a thread-safe manner.
        :param day_of_week: Day of the week (e.g., "Monday").
        :return: List of Flight objects.
        """
        with self.schedule_lock:  # Thread-safe block
            if day_of_week in self.operating_days:
                return [self.assigned_flight_instance]
            else:
                return []

    def get_schedule_details(self):
        """
        Get details of the schedule in a thread-safe manner.
        :return: Dictionary containing schedule details.
        """
        with self.schedule_lock:  # Thread-safe block
            return {
                "schedule_id": self.schedule_id,
                "route": self.route.get_route_details(),
                "departure_time": self.departure_time,
                "operating_days": self.operating_days,
                "assigned_flight_instance": self.assigned_flight_instance.flight_instance_id
            }

    def update_operating_days(self, new_operating_days):
        """
        Update the operating days of the schedule in a thread-safe manner.
        :param new_operating_days: List of new operating days.
        """
        with self.schedule_lock:  # Thread-safe block
            self.operating_days = new_operating_days
            print(f"Updated operating days for schedule {self.schedule_id}.")

class NotificationService:
    def send_booking_confirmation(self, passenger, booking):
        """
        Send a booking confirmation notification to the passenger.
        :param passenger: Passenger object to notify.
        :param booking: Booking object containing booking details.
        """
        message = f"Booking confirmed for flight {booking.flight_instance.flight.flight_number} on {booking.flight_instance.flight_date}."
        print(f"Notification sent to {passenger.name}: {message}")

    def send_flight_update(self, passenger, flight_instance):
        """
        Send a flight update notification to the passenger.
        :param passenger: Passenger object to notify.
        :param flight_instance: FlightInstance object containing flight details.
        """
        message = f"Flight {flight_instance.flight.flight_number} status updated to {flight_instance.flight_status}."
        print(f"Notification sent to {passenger.name}: {message}")

    def send_baggage_update(self, passenger, baggage):
        """
        Send a baggage update notification to the passenger.
        :param passenger: Passenger object to notify.
        :param baggage: Baggage object containing baggage details.
        """
        message = f"Baggage {baggage.baggage_id} status updated to {baggage.status}."
        print(f"Notification sent to {passenger.name}: {message}")

class ReportGenerator:
    def __init__(self, booking_manager, flight_manager, baggage_manager):
        """
        Initialize the ReportGenerator with references to BookingManager, FlightManager, and BaggageManager.
        """
        self.booking_manager = booking_manager
        self.flight_manager = flight_manager
        self.baggage_manager = baggage_manager

    def generate_revenue_report(self):
        """
        Generate a revenue report based on completed bookings.
        :return: Dictionary containing revenue details.
        """
        total_revenue = sum(booking.price for booking in self.booking_manager.get_all_bookings())
        return {"total_revenue": total_revenue}

    def generate_crew_schedule_report(self):
        """
        Generate a report of crew schedules for all flight instances.
        :return: Dictionary containing crew schedule details.
        """
        crew_schedule = {}
        for flight_instance in self.flight_manager.get_all_flight_instances():
            crew_schedule[flight_instance.flight_instance_id] = [crew.name for crew in flight_instance.assigned_crew]
        return crew_schedule

    def generate_baggage_report(self):
        """
        Generate a report of baggage details.
        :return: Dictionary containing baggage details.
        """
        baggage_report = {}
        for baggage in self.baggage_manager.get_all_baggage():
            baggage_report[baggage.baggage_id] = {
                "weight": baggage.weight,
                "status": baggage.status,
                "extra_fee": baggage.extra_fee
            }
        return baggage_report

class Airline:
    def __init__(self, airline_id, name, code):
        """
        Initialize an Airline object.
        :param airline_id: Unique ID for the airline.
        :param name: Name of the airline.
        :param code: Code of the airline (e.g., "BA" for British Airways).
        """
        self.airline_id = airline_id
        self.name = name
        self.code = code
        self.flights = []  # List to store flights operated by the airline

    def add_flight(self, flight):
        """
        Add a flight to the airline's list of flights.
        :param flight: Flight object to add.
        """
        self.flights.append(flight)
        print(f"Added flight {flight.flight_number} to airline {self.name}.")

    def remove_flight(self, flight):
        """
        Remove a flight from the airline's list of flights.
        :param flight: Flight object to remove.
        """
        if flight in self.flights:
            self.flights.remove(flight)
            print(f"Removed flight {flight.flight_number} from airline {self.name}.")
        else:
            print(f"Flight {flight.flight_number} is not operated by airline {self.name}.")

    def get_airline_details(self):
        """
        Get details of the airline.
        :return: Dictionary containing airline details.
        """
        return {
            "airline_id": self.airline_id,
            "name": self.name,
            "code": self.code,
            "flights": [flight.flight_number for flight in self.flights]
        }

class Airport:
    def __init__(self, airport_code, name, location):
        """
        Initialize an Airport object.
        :param airport_code: Unique code for the airport (e.g., "LHR" for London Heathrow).
        :param name: Name of the airport.
        :param location: Location of the airport.
        """
        self.airport_code = airport_code
        self.name = name
        self.location = location
        self.flights = []  # List to store flights operating at the airport

    def add_flight(self, flight):
        """
        Add a flight to the airport's list of flights.
        :param flight: Flight object to add.
        """
        self.flights.append(flight)
        print(f"Added flight {flight.flight_number} to airport {self.name}.")

    def remove_flight(self, flight):
        """
        Remove a flight from the airport's list of flights.
        :param flight: Flight object to remove.
        """
        if flight in self.flights:
            self.flights.remove(flight)
            print(f"Removed flight {flight.flight_number} from airport {self.name}.")
        else:
            print(f"Flight {flight.flight_number} is not operating at airport {self.name}.")

    def get_airport_details(self):
        """
        Get details of the airport.
        :return: Dictionary containing airport details.
        """
        return {
            "airport_code": self.airport_code,
            "name": self.name,
            "location": self.location,
            "flights": [flight.flight_number for flight in self.flights]
        }

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}.")
        return {"status": "Success", "method": "Credit Card", "amount": amount}

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing UPI payment of ${amount}.")
        return {"status": "Success", "method": "UPI", "amount": amount}

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}.")
        return {"status": "Success", "method": "PayPal", "amount": amount}

class PassengerFactory:
    def create_passenger(self, passenger_id, name, email, phone):
        return Passenger(passenger_id, name, email, phone)

class FlightFactory:
    def create_flight(self, flight_number, source, destination):
        return Flight(flight_number, source, destination)

class BookingFactory:
    def create_booking(self, booking_id, flight_instance, passenger, seat, price):
        return Booking(booking_id, flight_instance, passenger, seat, price)

class BookingDecorator:
    def __init__(self, booking):
        self.booking = booking

    def get_price(self):
        return self.booking.get_price()

class ExtraBaggageDecorator(BookingDecorator):
    def get_price(self):
        return self.booking.get_price() + 50  # $50 for extra baggage

class InFlightMealDecorator(BookingDecorator):
    def get_price(self):
        return self.booking.get_price() + 20  # $20 for in-flight meal

class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, request):
        pass

class SearchFlightHandler(Handler):
    def handle(self, request):
        if request == "search":
            print("Searching for flights...")
        elif self.next_handler:
            self.next_handler.handle(request)

class SelectSeatHandler(Handler):
    def handle(self, request):
        if request == "select_seat":
            print("Selecting seat...")
        elif self.next_handler:
            self.next_handler.handle(request)

class MakePaymentHandler(Handler):
    def handle(self, request):
        if request == "make_payment":
            print("Processing payment...")
        elif self.next_handler:
            self.next_handler.handle(request)

class ATC:
    def update_flight_status(self, flight, status):
        print(f"ATC notified: Flight {flight.flight_number} status updated to {status}.")

class Mediator:
    def __init__(self):
        self.flights = []
        self.atc = ATC()

    def register_flight(self, flight):
        self.flights.append(flight)

    def notify_atc(self, flight, status):
        self.atc.update_flight_status(flight, status)