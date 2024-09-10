package ChainHandler;

public class RequestClass {
    String msg;
    Priority priority;

    public RequestClass(String msg, Priority priority){
        this.msg = msg;
        this.priority = priority;
    }

    public Priority getPriority(){
        return this.priority;
    }
}
