from dataclasses import dataclass
from datetime import datetime
from typing import List
from enums import BookingStatus, SeatStatus, SeatType
from Models import Movie, ShowSeat, Booking

@dataclass
class MovieDTO:
    id: str
    title: str
    duration: int
    language: str
    genre: str

    @classmethod
    def from_model(cls, movie: 'Movie') -> 'MovieDTO':
        return cls(
            id=movie.id,
            title=movie.title,
            duration=movie.duration,
            language=movie.language,
            genre=movie.genre
        )

@dataclass
class ShowSeatDTO:
    id: str
    seat_number: str
    seat_type: SeatType
    price: float
    status: SeatStatus

    @classmethod
    def from_model(cls, show_seat: 'ShowSeat') -> 'ShowSeatDTO':
        return cls(
            id=show_seat.id,
            seat_number=show_seat.hall_seat.seat_number,
            seat_type=show_seat.hall_seat.seat_type,
            price=show_seat.price,
            status=show_seat.status
        )

@dataclass
class BookingDTO:
    id: str
    customer_name: str
    movie_title: str
    show_time: datetime
    seats: List[str]
    total_amount: float
    status: BookingStatus

    @classmethod
    def from_model(cls, booking: 'Booking') -> 'BookingDTO':
        return cls(
            id=booking.id,
            customer_name=booking.customer.name,
            movie_title=booking.show.movie.title,
            show_time=booking.show.start_time,
            seats=[seat.hall_seat.seat_number for seat in booking.seats],
            total_amount=booking.total_amount,
            status=booking.status
        )