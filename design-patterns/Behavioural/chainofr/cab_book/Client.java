package cab_book;

public class Client {
    public static void main(String[] args) {
        RideBookingHandler rideBookingHandler = new RideBookingHandler(null);
        PaymentProcessorHandler paymentProcessorHandler = new PaymentProcessorHandler(rideBookingHandler);
        PastPaymentHandler pastPaymentHandler = new PastPaymentHandler(paymentProcessorHandler);
        AccountHandler accountHandler = new AccountHandler(pastPaymentHandler);
        AuthenticationHandler authenticationHandler = new AuthenticationHandler(accountHandler);

        Request request = new Request(RequestType.BOOK_A_RIDE, "123456");

        authenticationHandler.handle(request);

        System.out.println("request.status = " + request.getRequestStatus());
    }
}
