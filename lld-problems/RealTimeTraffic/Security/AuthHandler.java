package Security;

public class AuthHandler extends SecurityHandler{
    @Override
    public void handle(String request){
        if(request.equals("auth")){
            System.out.println("Auth handled");
        }
        else if(super.nextHandler() != null){
            super.nextHandler().handle(request);
        }
    }
}
