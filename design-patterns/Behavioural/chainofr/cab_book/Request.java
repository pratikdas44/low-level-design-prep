package cab_book;

public class Request {
    private RequestStatus requestStatus;
    private PaymentStatus paymentStatus;
    private RequestType requestType;
    private String userId;
    private String authToken;

    public Request(RequestType requestType, String token){
        this.requestType = requestType;
        this.authToken = token;
        this.requestStatus = RequestStatus.IN_PROGRESS;
        this.paymentStatus = PaymentStatus.UNKNOWN;
        this.userId = null;
    }


    public RequestStatus getRequestStatus() {
        return this.requestStatus;
    }

    public void setRequestStatus(RequestStatus requestStatus) {
        this.requestStatus = requestStatus;
    }

    public PaymentStatus getPaymentStatus() {
        return this.paymentStatus;
    }

    public void setPaymentStatus(PaymentStatus paymentStatus) {
        this.paymentStatus = paymentStatus;
    }

    public RequestType getRequestType() {
        return this.requestType;
    }

    public void setRequestType(RequestType requestType) {
        this.requestType = requestType;
    }

    public String getUserId() {
        return this.userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getAuthToken() {
        return this.authToken;
    }

    public void setAuthToken(String authToken) {
        this.authToken = authToken;
    }


}
