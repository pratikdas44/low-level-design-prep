package Security;

public abstract class SecurityHandler {
    private SecurityHandler securityHandler;
    public void setSuccessor(SecurityHandler securityHandler){
        this.securityHandler = securityHandler;
    }
    public abstract void handle(String request);
    public SecurityHandler nextHandler(){
        return securityHandler;
    }
}
