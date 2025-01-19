from enum import Enum

class BookingStatus(Enum):
    PAYMENT_PENDING = 1
    SUCCESS = 2
    FAILURE = 3