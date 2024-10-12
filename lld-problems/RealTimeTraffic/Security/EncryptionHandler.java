package Security;

public class EncryptionHandler extends SecurityHandler{

    @Override
    public void handle(String request){
        if(request.equals("encrypt")){
            System.out.println("Encryption handled");
        }
        else if(super.nextHandler() != null){
            super.nextHandler().handle(request);
        }
    }
}
