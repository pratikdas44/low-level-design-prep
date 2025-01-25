# main.py
from datetime import datetime, timedelta
from Models import City, Cinema, Hall, SeatType, HallSeat, Customer, Movie, Show
from services import MovieService, BookingService
from repository import MovieRepository, ShowRepository, BookingRepository, CustomerRepository
import time
from typing import Tuple, List
import threading
from enums import BookingStatus

def initialize_system() -> Tuple[MovieService, BookingService, MovieRepository, ShowRepository, CustomerRepository]:
    # Initialize repositories
    movie_repo = MovieRepository()
    show_repo = ShowRepository()
    booking_repo = BookingRepository()
    customer_repo = CustomerRepository()

    # Initialize services
    movie_service = MovieService(movie_repo)
    booking_service = BookingService(booking_repo, show_repo, customer_repo)

    return movie_service, booking_service, movie_repo, show_repo, customer_repo

def setup_test_data(movie_repo: MovieRepository, 
                   show_repo: ShowRepository, 
                   customer_repo: CustomerRepository) -> Tuple[Show, List[Customer]]:
    # Create city and cinema hierarchy
    city = City("Mumbai")
    cinema = Cinema("PVR", "Main Street", city)
    
    # Create hall with seats
    hall = Hall("Screen 1", cinema, 100)
    for row in "ABC":
        for num in range(1, 5):
            seat_type = SeatType.PREMIUM if row == 'A' else SeatType.REGULAR
            HallSeat(f"{row}{num}", hall, seat_type)

    # Create movie and show
    movie = Movie("Inception", 150, "English", "Sci-Fi")
    movie_repo.save(movie)

    show_time = datetime.now() + timedelta(days=1)
    show = Show(movie, hall, show_time)
    show_repo.save(show)

    # Create multiple customers for testing
    customers = [
        Customer("John Doe", "john@example.com", "1234567890"),
        Customer("Jane Smith", "jane@example.com", "9876543210"),
        Customer("Bob Wilson", "bob@example.com", "5555555555")
    ]
    
    for customer in customers:
        customer_repo.save(customer)

    return show, customers

def simulate_concurrent_booking(booking_service: BookingService, 
                              customer: Customer, 
                              show: Show, 
                              seats: List[str],
                              thread_name: str) -> None:
    try:
        print(f"\n{thread_name} attempting to book seats: {seats}")
        booking_dto = booking_service.create_booking(customer.id, show.id, seats)
        print(f"\n{thread_name} Successfully booked!")
        print(f"Booking Details:")
        print(f"Booking ID: {booking_dto.id}")
        print(f"Customer: {booking_dto.customer_name}")
        print(f"Movie: {booking_dto.movie_title}")
        print(f"Seats: {', '.join(booking_dto.seats)}")
        print(f"Total amount: ${booking_dto.total_amount}")
        print(f"Status: {booking_dto.status.value}")
    except ValueError as e:
        print(f"\n{thread_name} Booking failed: {str(e)}")

def test_single_booking(booking_service: BookingService, 
                       customer: Customer, 
                       show: Show) -> None:
    print("\nTesting single booking scenario...")
    try:
        seats_to_book = ["A1", "A2"]
        booking_dto = booking_service.create_booking(customer.id, show.id, seats_to_book)
        
        print("\nBooking created successfully!")
        print(f"Booking ID: {booking_dto.id}")
        print(f"Customer: {booking_dto.customer_name}")
        print(f"Movie: {booking_dto.movie_title}")
        print(f"Show time: {booking_dto.show_time}")
        print(f"Seats: {', '.join(booking_dto.seats)}")
        print(f"Total amount: ${booking_dto.total_amount}")
        print(f"Status: {booking_dto.status.value}")  # Should now show CONFIRMED

        if booking_dto.status == BookingStatus.CONFIRMED:
            print("Payment successful and booking confirmed!")

        # Test cancellation
        cancelled_booking = booking_service.cancel_booking(booking_dto.id)
        print("\nBooking cancelled successfully!")
        print(f"Status: {cancelled_booking.status.value}")

    except ValueError as e:
        print(f"Error: {e}")

def test_concurrent_bookings(booking_service: BookingService, 
                           customers: List[Customer], 
                           show: Show) -> None:
    print("\nTesting concurrent booking scenario...")
    
    # Create threads for concurrent booking attempts
    threads = []
    
    # Same seats, different customers
    same_seats = ["A1", "A2"]
    thread1 = threading.Thread(
        target=simulate_concurrent_booking,
        args=(booking_service, customers[0], show, same_seats, "Thread 1")
    )
    thread2 = threading.Thread(
        target=simulate_concurrent_booking,
        args=(booking_service, customers[1], show, same_seats, "Thread 2")
    )
    threads.extend([thread1, thread2])

    # Different seats, different customers
    thread3 = threading.Thread(
        target=simulate_concurrent_booking,
        args=(booking_service, customers[2], show, ["B1", "B2"], "Thread 3")
    )
    threads.append(thread3)

    # Start all threads
    for thread in threads:
        thread.start()
        time.sleep(0.1)  # Small delay to make output more readable

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

def test_seat_availability(booking_service: BookingService, show: Show) -> None:
    print("\nTesting seat availability...")
    seats_to_check = ["A1", "A2"]
    
    try:
        is_available = booking_service.check_seat_availability(show.id, seats_to_check)
        print(f"Seats {seats_to_check} availability: {'Available' if is_available else 'Not Available'}")
    except ValueError as e:
        print(f"Error checking availability: {e}")

def main():
    # Initialize system
    movie_service, booking_service, movie_repo, show_repo, customer_repo = initialize_system()

    try:
        # Setup test data
        show, customers = setup_test_data(movie_repo, show_repo, customer_repo)
        
        # Test 1: Single booking scenario
        test_single_booking(booking_service, customers[0], show)
        
        # Test 2: Concurrent booking scenarios
        test_concurrent_bookings(booking_service, customers, show)
        
        # Test 3: Seat availability check
        test_seat_availability(booking_service, show)

    except Exception as e:
        print(f"System Error: {e}")
        
    finally:
        print("\nTest scenarios completed.")

if __name__ == "__main__":
    main()