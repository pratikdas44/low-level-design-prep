package cab_book;
public class AuthenticationHandler extends RequestHandler {

    public AuthenticationHandler(RequestHandler nextHandler) {
        super(nextHandler);
    }

    @Override
    public void handle(Request request) {
        if (request.getAuthToken() != null) {
            request.setUserId("123");
            if (super.nextHandler() != null) {
                super.nextHandler().handle(request);
            }
        }
    }
}
