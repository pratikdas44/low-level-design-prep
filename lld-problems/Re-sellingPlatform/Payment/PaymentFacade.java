package Payment;

public class PaymentFacade {
    private PaymentGateway paymentGateway;
    public PaymentFacade(PaymentGateway paymentGateway){
        this.paymentGateway = paymentGateway;
    }

    public boolean processPayment(double amount, String card, String cvv, String expire){
        return paymentGateway.processPayment(amount, card, cvv, expire);
    }
}
