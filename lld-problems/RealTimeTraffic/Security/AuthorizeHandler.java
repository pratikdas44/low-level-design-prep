package Security;

public class AuthorizeHandler extends SecurityHandler{

    @Override
    public void handle(String request){
        if(request.equals("authorize")){
            System.out.println("Encryption handled");
        }
        else if(super.nextHandler() != null){
            super.nextHandler().handle(request);
        }
    }
}