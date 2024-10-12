package Payment;

public interface PaymentGateway {
    public boolean processPayment(double amount, String card, String cvv, String expire);
}
