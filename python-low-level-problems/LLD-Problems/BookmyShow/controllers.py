class BookingController():
    def __init__(self):
        self.bookingService = None

    def bookTicket(self, bookingRequest):
        return bookingRequest.bookTicket(bookingRequest)
        

class CustomerController():
    def __init__(self):
        self.customerService = None

    def createCustomer(self, customerRequest):
        self.customerService.createCustomer(customerRequest)


class MovieController():
    def __init__(self):
        self.movieService = None

    def requestMethodName(self):
        return self.movieService.listMovies()
    