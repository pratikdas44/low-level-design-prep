package cab_book;

public abstract class RequestHandler {
    private RequestHandler requestHandler;

    public RequestHandler(RequestHandler requestHandler){
        this.requestHandler = requestHandler;
    }

    abstract void handle(Request request);
    
    public RequestHandler nextHandler(){
        return requestHandler;
    }
}
