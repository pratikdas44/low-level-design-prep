from datetime import datetime
from abc import ABC
from uuid import uuid4
from typing import List
from enums import SeatStatus, BookingStatus, SeatType

class BaseModel(ABC):
    def __init__(self):
        self.id: str = str(uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()

class City(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name: str = name
        self.cinemas: List['Cinema'] = []

    def add_cinema(self, cinema: 'Cinema') -> None:
        self.cinemas.append(cinema)

class Cinema(BaseModel):
    def __init__(self, name: str, address: str, city: City):
        super().__init__()
        self.name: str = name
        self.address: str = address
        self.city: City = city
        self.halls: List['Hall'] = []
        city.add_cinema(self)

    def add_hall(self, hall: 'Hall') -> None:
        self.halls.append(hall)

class Hall(BaseModel):
    def __init__(self, name: str, cinema: Cinema, capacity: int):
        super().__init__()
        self.name: str = name
        self.cinema: Cinema = cinema
        self.capacity: int = capacity
        self.seats: List['HallSeat'] = []
        cinema.add_hall(self)

    def add_seat(self, seat: 'HallSeat') -> None:
        self.seats.append(seat)

class HallSeat(BaseModel):
    def __init__(self, seat_number: str, hall: Hall, seat_type: SeatType):
        super().__init__()
        self.seat_number: str = seat_number
        self.hall: Hall = hall
        self.seat_type: SeatType = seat_type
        hall.add_seat(self)

class Movie(BaseModel):
    def __init__(self, title: str, duration: int, language: str, genre: str):
        super().__init__()
        self.title: str = title
        self.duration: int = duration
        self.language: str = language
        self.genre: str = genre

class Show(BaseModel):
    def __init__(self, movie: Movie, hall: Hall, start_time: datetime):
        super().__init__()
        self.movie: Movie = movie
        self.hall: Hall = hall
        self.start_time: datetime = start_time
        self.show_seats: List['ShowSeat'] = []
        self._initialize_show_seats()

    def _initialize_show_seats(self) -> None:
        for hall_seat in self.hall.seats:
            price = self._get_base_price(hall_seat.seat_type)
            show_seat = ShowSeat(hall_seat, self, price)
            self.show_seats.append(show_seat)

    def _get_base_price(self, seat_type: SeatType) -> float:
        price_map = {
            SeatType.REGULAR: 100.0,
            SeatType.PREMIUM: 200.0,
            SeatType.VIP: 300.0
        }
        return price_map[seat_type]

class ShowSeat(BaseModel):
    def __init__(self, hall_seat: HallSeat, show: Show, price: float):
        super().__init__()
        self.hall_seat: HallSeat = hall_seat
        self.show: Show = show
        self.status: SeatStatus = SeatStatus.AVAILABLE
        self.price: float = price

class User(BaseModel):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__()
        self.name: str = name
        self.email: str = email
        self.phone: str = phone

class Customer(User):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__(name, email, phone)
        self.bookings: List['Booking'] = []

    def add_booking(self, booking: 'Booking') -> None:
        self.bookings.append(booking)

class Booking(BaseModel):
    def __init__(self, customer: Customer, show: Show):
        super().__init__()
        self.customer: Customer = customer
        self.show: Show = show
        self.seats: List[ShowSeat] = []
        self.status: BookingStatus = BookingStatus.PENDING
        self.total_amount: float = 0