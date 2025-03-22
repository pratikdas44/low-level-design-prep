import unittest
from models.person import Payment, CreditCardPayment, UPIPayment, PayPalPayment

class TestPayment(unittest.TestCase):
    def test_credit_card_payment(self):
        strategy = CreditCardPayment()
        payment = Payment(1, "Credit Card", 200)  # Pass "Credit Card" as the payment method
        result = payment.process_payment()
        self.assertEqual(result["status"], "Success")
        self.assertEqual(result["method"], "Credit Card")  # This should now pass
        self.assertEqual(result["amount"], 200)

    def test_upi_payment(self):
        strategy = UPIPayment()
        payment = Payment(2, "UPI", 150)  # Pass "UPI" as the payment method
        result = payment.process_payment()
        self.assertEqual(result["status"], "Success")
        self.assertEqual(result["method"], "UPI")  # This should now pass
        self.assertEqual(result["amount"], 150)

    def test_paypal_payment(self):
        strategy = PayPalPayment()
        payment = Payment(3, "PayPal", 300)  # Pass "PayPal" as the payment method
        result = payment.process_payment()
        self.assertEqual(result["status"], "Success")
        self.assertEqual(result["method"], "PayPal")  # This should now pass
        self.assertEqual(result["amount"], 300)