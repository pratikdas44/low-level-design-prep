package ChainHandler;

public class Type1RequestHandler extends RequestHandler{
    public Type1RequestHandler(RequestHandler nextHandler){
        super(nextHandler);
    }

    @Override
    public void handle(RequestClass requestClass){
        if(requestClass.getPriority().equals(Priority.HIGH)){
            System.out.println("Request assigned to Type 1");
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
