package Payment;

public class Main {
    public static void main(String[] args) {
        PaymentGateway paymentGateway = new StripePaymentGateway();
        PaymentFacade facade = new PaymentFacade(paymentGateway);
        boolean success = facade.processPayment(100.0, "1234", "1", "12/24");
        System.out.println("Payment successfull " + success);
    }
}
