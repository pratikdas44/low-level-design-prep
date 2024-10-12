package Security;

public class CORDemo {
    public static void main(String[] args) {
        SecurityHandler securityHandler = new AuthHandler();
        SecurityHandler encryptHandler = new EncryptionHandler();
        SecurityHandler authHandler = new AuthorizeHandler();
        authHandler.setSuccessor(securityHandler);
        securityHandler.setSuccessor(encryptHandler);
        authHandler.handle("encrypt");
        authHandler.handle("auth");
    }
}
