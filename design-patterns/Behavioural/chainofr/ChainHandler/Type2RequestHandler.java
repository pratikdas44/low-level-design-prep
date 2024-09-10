package ChainHandler;

public class Type2RequestHandler extends RequestHandler{
    public Type2RequestHandler(RequestHandler nextHandler){
        super(nextHandler);
    }

    @Override
    public void handle(RequestClass requestClass){
        if(requestClass.getPriority().equals(Priority.MEDIUM)){
            System.out.println("Request assigned to Type 2");
        }
        else if(super.getnextHandler() != null){
            System.out.println("Skipping current handler " + requestClass.getPriority());
            super.getnextHandler().handle(requestClass);
        }
        else{
            System.out.println("Out of scope");
        }
    }
}