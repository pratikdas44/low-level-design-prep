package ChainHandler;

public abstract class RequestHandler{
    private RequestHandler nextHandler;

    public RequestHandler(RequestHandler nextHandler){
        this.nextHandler = nextHandler;
    }

    public RequestHandler getnextHandler(){
        return this.nextHandler;
    }

    public abstract void handle(RequestClass requestClass);
}
