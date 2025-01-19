from datetime import datetime

class Auditable():
    def __init__(self, id, created, updated):
        self.id = id
        self.created = created
        self.updated = updated

class Admin(Auditable):
    def __init__(self, designation, phone, years, user):
        self.designation = designation
        self.phone = phone
        self.years = years
        self.user = user

class Booking(Auditable):
    def __init__(self, customer, show, status):
        self.customer = customer
        self.show = show
        self.status = status
        self.seatsBooked = []

class Cinema(Auditable):
    def __init__(self):
        self.name = ""
        self.address = ""
        self.halls = []

class CinemaHall(Auditable):
    def __init__(self):
        self.hallNumber = ""
        self.seatcount = 0
        self.cinema = None
        self.halls = []

class Customer(Auditable):
    def __init__(self):
        self.fullName = ""
        self.phone = ""
        self.city = ""
        self.email = ""
        self.bookings = []
        self.user = None

class HallSeat(Auditable):
    def __init__(self):
        self.seatLocation = ""
        self.seatType = 0
        self.cinemaHall = None
        self.showSeats = []

class Movie(Auditable):
    def __init__(self):
        self.name = ""
        self.duration = 0
        self.shows = []

class Role(Auditable):
    def __init__(self):
        self.name = ""
        self.description = ""

class Show(Auditable):
    def __init__(self):
        self.startTime = None  # Use datetime for start and end time
        self.endTime = None
        self.movie = None
        self.cinemaHall = None
        self.cancelled = False
        self.bookings = []
        self.showSeats = []
    
    def isShowPending(self):
        if self.cancelled:
            return False
        if self.endTime and self.endTime > datetime.now():
            return True
        return False
    
class ShowSeat(Auditable):
    def __init__(self):
        self.hallSeat = None
        self.show = None
        self.booking = None
        self.occupied = None

class User(Auditable):
    def __init__(self, username):
        self.userName = username
        self.password = None
        self.roles = set()
    
    def setPassword(self, password):
        self.password = password




