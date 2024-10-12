package Payment;

public class StripePaymentGateway implements PaymentGateway{
    @Override
    public boolean processPayment(double amount, String card, String cvv, String expire){
        return true;
    }
}
