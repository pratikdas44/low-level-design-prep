# Airline Management System

This is a Python-based Airline Management System that allows users to manage flights, bookings, passengers, and payments.

## Features
- Create and manage flights.
- Book seats for passengers.
- Process payments.
- Generate reports.

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   

1. User should be able to search flights, book flights, update details, create account and update account details, view booking history and view flight details.
2. Crew consists of Air hoistess and Pilot. Pilot will be always communicating with ATC
3. Baggage tracking system and baggage weight limits
4. Admin should be able to add flights, cancel flights, see bookings and see the allocated employee with the flight
5. user will book the flight based on date, source and destination and timings, they will select seats and make payment.
6. system should handle cancellation, refunds and flight changes, customer should be able to cancel their reservation.
7. user can make reservations for multiple passengers under one booking
8. system should be able to handle the assignment of pilots and crew members to flights.
9. system should send notifications to customers whenever a reservation is made or there is update for flights.

UseCase:
1. Admin -> add/modify aircraft, add/modify flight, add/modify flightschedule, modify flight instance <- extends <- assign pilot/crew, cancel flight instance, view flight instance
2. User or Front desk officer: search flight, book reservation -> includes -> add passenger -> includes -> select seat, make payment, update/cancel/view reservation, login/logout/reset pass, cancel reservation -> includes -> refund, cancel reservation -> includes -> send notification
3. system -> send reservation notification, send flight status update notification

Clases:
1. System - entry point.
    a. Attributes - <passengers>, <flights>, <crewMembers>, <aircrafts>, <bookings>, <payments>
    b. Methods - initializeSystem(), getSystemStatus(), generateReport()

2. passenger:
    a. passengerId, name, email, phone, list<booking>
    b. updateDetails(name, email, phone), getBookingHistory(), initiatePayment(Booking booking, PaymentMethod method)

3. crewMember:
    a. id, name, email, phone number, role, exp_year, license_id, list<FlightInstance>
    b. getAssignedFlightInstance()

4. flight:
    a. flight number, source, destination, scheduled_departure, scheduled_arrival, operatingDays, aircraft, price_per_seat, bag_allowance, extra_baggage_fee
    b. addOperatingDay(day), removeOperatingDay(day), getFlightInstances(startDate, endDate), removeFlight(), getFlightDetails()


5. FlightInstance:
    a. flightInstanceId, flight, actualDepature, actualArrival, flightDate, availableSeats, flightStatus, assginedCrewa
    b. assignCrew(CrewMember crew), updateStatus(FlightStatus status), getAvailableSeats(), calculateRevenue(), getFlightInstanceDetails(), calculateOccupancy()

6. aircraft:
    a. id, model, total_seats, list<flightInstance>
    b. assignToFlightInstance(FlightInstance flightInstance), getassignedFlightInstances(), getAircraftDetails(), removeFromFlightInstance(flightInstance)

7. Booking:
    a. booking_id, flightInstance, passenger, seat, price, booking_status, cancellation_fee, refund_status, booking_timestamp
    b. cancelBooking(), calculateRefund(), updateSeat(Seat newSeat), updateBookingStatus(bookingStatus), getBookingDetails()

8. Seat:
    a. seat_number, seat_type and seat_status
    b. isAvailable(), reserveSeat(), updateStatus(SeatStatus status), getSeatDetails(), isWindowSeat()

9. Payment:
    a. payment_id, pay_method, amount, pay_status, payment_date, txn_id
    b. processPayment(), refundPayment(), getPaymentDetails()

10. Booking manager:
    a. list<Booking>
    b. createBooking(passenger, flightInstance, seat), cancelBooking(booking), getBookingDetails(booking), generateBookingreport(), updateBooking(booking), getAllBookings()

11. PaymentProcessor:
    a. list<payment>
    b. processPayment(Payment payment), refundPayment(Payment payment), validatePayment(Payment payment), getAllPayments(), generatePaymentReport()

12. FlightManager:
    a. list<flight>, list<flightInstance>
    b. createFlightTemplate(src, dest), createFlightInstance(flight, flightDate), updateFlightInstanceStatus(flightInstance, flightStatus), assignCrewToFlightInstance(flightInstance, List<CrewMember>), searchFlight(src, dest, date), getAllFlights(), getAllFlightInstances()

13. FlightSearch:
    a. list<flightInstances>
    b. searchByRoute(src, dest), searchByDate(depatureDate)

14. baggage:
    a. baggage_id, weight and status, extra_fee
    b. calculateExtraFee(), updateStatus(bagStatus), getBagDetails(), calculateTotalFee()

15. route class:
    a. routeId, origin, destination, distance, duration
    b. getDistance(), getDuration(), updateRoute(newSrc, newDst), getRouteDetails(), calculateTravelTime()

16. flightschedule:
    a. scheduleId, route, departureTime, operatingDays, assignedFlightInstance
    b. addFlightToSchedule(flight), removeFlightFromSchedule(flight), getFlightsByDay(dayofWeek), getScheduleDetails(), updateOperatingDays(List<DayofWeek> days)

17. notificationService:
    b. sendBookingConfirmation(passenger, booking), sendFlightUpdate(passenger, flightInstance), sendBaggageUpdate(passenger, baggage)

18. ReportGenerator:
    b. generateRevenueReport(), generateCrewScheduleReport(), generateBaggageReport()

19. Airline:
    a. airlineId, name, code, list<flight>
    b. addFlight(flight), removeFlight(flight), getAirlineDetails()

20. Airport:
    a. airportCode, name, location, list<flight>
    b. addFlight(flight), removeFlight(flight), getAirportDetails()

Design pattern:
1. facade for airlinemanagesystem
2. singleton - paymentprocessor, booking manager, airlinemanagementsystem
3. mediator design pattern between atc and flight
4. startegy for payment or adapter class for payment
5. chain of responsibility -> search flight, book flight, select seat, make payment, get seat
6. observer pattern to receive flight notifications
7. factory - passenger, booking, flight
8. decorator - add additional services eg - extra baggage, inflight meals, seat upgrades without modifying booking class
9.

Concurrency:
1. multiple user booking same seat - double booking. Use locking or atomic txn
2. duplicate cancellations - pessimistic locking