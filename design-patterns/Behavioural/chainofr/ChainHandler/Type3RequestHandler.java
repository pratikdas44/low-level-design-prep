package ChainHandler;

public class Type3RequestHandler extends RequestHandler{
    public Type3RequestHandler(RequestHandler nextHandler){
        super(nextHandler);
    }

    @Override
    public void handle(RequestClass requestClass){
        if(requestClass.getPriority().equals(Priority.LOW)){
            System.out.println("Request assigned to Type 3");
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