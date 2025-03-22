from enum import Enum

# Seat status constants
class SeatStatus:
    AVAILABLE = "Available"
    BOOKED = "Booked"

# Flight status constants
class FlightStatus:
    SCHEDULED = "Scheduled"
    DELAYED = "Delayed"
    CANCELLED = "Cancelled"

# Booking status constants
class BookingStatus:
    CONFIRMED = "Confirmed"
    PENDING = "Pending"
    CANCELLED = "Cancelled"

# Payment status constants
class PaymentStatus:
    SUCCESS = "Success"
    FAILED = "Failed"
    PENDING = "Pending"
    REFUNDED = "Refunded"

# Payment method enum
class PaymentMethod(Enum):
    CREDIT_CARD = "Credit Card"
    UPI = "UPI"
    PAYPAL = "PayPal"

# Seat type enum
class SeatType(Enum):
    ECONOMY = "Economy"
    BUSINESS = "Business"
    FIRST_CLASS = "First Class"

# Baggage status enum
class BaggageStatus(Enum):
    CHECKED_IN = "Checked-In"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
