package cab_book;
public class AccountHandler extends RequestHandler{

    public AccountHandler(RequestHandler requestHandler){
        super(requestHandler);
    }

    @Override
    public void handle(Request request){
        if(request.getUserId() != null){
            if(super.nextHandler() != null){
                super.nextHandler().handle(request);
            }
        }
    }
}
