import unittest
from models.person import SearchFlightHandler, SelectSeatHandler, MakePaymentHandler

class TestChainOfResponsibility(unittest.TestCase):
    def test_chain_of_responsibility(self):
        search_handler = SearchFlightHandler()
        select_seat_handler = SelectSeatHandler()
        make_payment_handler = MakePaymentHandler()

        search_handler.next_handler = select_seat_handler
        select_seat_handler.next_handler = make_payment_handler

        # Test search handler
        search_handler.handle("search")
        # Test select seat handler
        search_handler.handle("select_seat")
        # Test make payment handler
        search_handler.handle("make_payment")