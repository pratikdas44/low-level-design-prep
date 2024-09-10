package ChainHandler;

public class Main {
    public static void main(String[] args) {
        RequestClass requestClass = new RequestClass("Type1 Task", Priority.HIGH);
        RequestHandler type1RequestHandler = new Type1RequestHandler(null);
        RequestHandler type2RequestHandler = new Type2RequestHandler(type1RequestHandler);
        RequestHandler type3RequestHandler = new Type3RequestHandler(type2RequestHandler);

        type3RequestHandler.handle(requestClass);
    }
}
