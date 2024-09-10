package cab_book;

public class RideBookingHandler extends RequestHandler {
    public RideBookingHandler(RequestHandler nextHandler) {
        super(nextHandler);
    }

    @Override
    void handle(Request request) {
        if (request.getPaymentStatus() == PaymentStatus.COMPLETE && request.getRequestType() == RequestType.BOOK_A_RIDE) {
            // book a ride here
            System.out.println("Booking a ride here!");
            request.setRequestStatus(RequestStatus.SUCCESS);
        }
        if (super.nextHandler() != null) {
            super.nextHandler().handle(request);
        }
    }
}
