# services/movie_service.py
from typing import List, Optional, Dict
from Models import Movie
from repository import MovieRepository, BookingRepository, ShowRepository, CustomerRepository, Booking
from dto import MovieDTO, BookingDTO
from enums import SeatStatus, BookingStatus
from threading import Lock
from datetime import datetime
import time


class MovieService:
    def __init__(self, movie_repository: MovieRepository):
        self._repository = movie_repository

    def add_movie(self, title: str, duration: int, language: str, genre: str) -> MovieDTO:
        movie = Movie(title, duration, language, genre)
        saved_movie = self._repository.save(movie)
        return MovieDTO.from_model(saved_movie)

    def get_movie(self, movie_id: str) -> Optional[MovieDTO]:
        movie = self._repository.get_by_id(movie_id)
        return MovieDTO.from_model(movie) if movie else None

class BookingService:
    def __init__(self, booking_repository: BookingRepository, 
                 show_repository: ShowRepository,
                 customer_repository: CustomerRepository):
        self._booking_repository = booking_repository
        self._show_repository = show_repository
        self._customer_repository = customer_repository
        self._show_locks: Dict[str, Lock] = {}  # Lock per show
        self._booking_locks: Dict[str, Lock] = {}  # Lock per booking

    def _get_show_lock(self, show_id: str) -> Lock:
        """Get or create a lock for a specific show"""
        if show_id not in self._show_locks:
            self._show_locks[show_id] = Lock()
        return self._show_locks[show_id]

    def _get_booking_lock(self, booking_id: str) -> Lock:
        """Get or create a lock for a specific booking"""
        if booking_id not in self._booking_locks:
            self._booking_locks[booking_id] = Lock()
        return self._booking_locks[booking_id]

    def create_booking(self, customer_id: str, show_id: str, 
                      seat_numbers: List[str]) -> BookingDTO:
        # Get show lock
        show_lock = self._get_show_lock(show_id)
        
        with show_lock:  # Thread-safe block for show-related operations
            show = self._show_repository.get_by_id(show_id)
            if not show:
                raise ValueError("Show not found")

            customer = self._customer_repository.get_by_id(customer_id)
            if not customer:
                raise ValueError("Customer not found")

            # Find and validate seats
            selected_seats = []
            for seat_number in seat_numbers:
                seat = next((s for s in show.show_seats 
                           if s.hall_seat.seat_number == seat_number), None)
                
                if not seat:
                    raise ValueError(f"Seat {seat_number} does not exist")
                
                # Check if seat is available - atomic operation within lock
                if seat.status != SeatStatus.AVAILABLE:
                    raise ValueError(f"Seat {seat_number} is not available")
                    
                selected_seats.append(seat)

            # Create booking with PENDING status
            booking = Booking(customer, show)
            booking.seats = selected_seats
            booking.total_amount = sum(seat.price for seat in selected_seats)
            booking.status = BookingStatus.PENDING  # Default status

            # Simulate payment process
            payment_success = self._process_payment(booking)
            
            if payment_success:
                # If payment successful, mark seats as BOOKED and confirm booking
                for seat in selected_seats:
                    seat.status = SeatStatus.BOOKED
                booking.status = BookingStatus.CONFIRMED
            else:
                # If payment fails, release seats and mark booking as CANCELLED
                booking.status = BookingStatus.CANCELLED
                raise ValueError("Payment failed")

            # Save the changes
            saved_booking = self._booking_repository.save(booking)
            customer.add_booking(saved_booking)
            self._customer_repository.save(customer)
            self._show_repository.save(show)

            return BookingDTO.from_model(saved_booking)

    def _process_payment(self, booking: Booking) -> bool:
        """
        Simulate payment processing
        In real implementation, this would integrate with a payment gateway
        """
        try:
            # Simulate successful payment
            time.sleep(1)  # Simulate payment processing time
            return True
        except Exception:
            return False

    def cancel_booking(self, booking_id: str) -> BookingDTO:
        booking = self._booking_repository.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")

        # Get both locks to prevent deadlocks
        booking_lock = self._get_booking_lock(booking_id)
        show_lock = self._get_show_lock(booking.show.id)
        
        # Acquire locks in a consistent order to prevent deadlocks
        with booking_lock, show_lock:
            if booking.status == BookingStatus.CANCELLED:
                raise ValueError("Booking is already cancelled")

            booking.status = BookingStatus.CANCELLED
            
            # Release seats
            for seat in booking.seats:
                seat.status = SeatStatus.AVAILABLE

            # Save changes
            saved_booking = self._booking_repository.save(booking)
            self._show_repository.save(booking.show)
            
            return BookingDTO.from_model(saved_booking)

    def check_seat_availability(self, show_id: str, seat_numbers: List[str]) -> bool:
        """Check if seats are available without making a booking"""
        show_lock = self._get_show_lock(show_id)
        
        with show_lock:
            show = self._show_repository.get_by_id(show_id)
            if not show:
                raise ValueError("Show not found")

            for seat_number in seat_numbers:
                seat = next((s for s in show.show_seats 
                           if s.hall_seat.seat_number == seat_number), None)
                
                if not seat or seat.status != SeatStatus.AVAILABLE:
                    return False
                    
            return True