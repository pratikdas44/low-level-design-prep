package UserAuthentication;

public class Main {
    public static void main(String[] args) {
        AuthenticationManager authenticationManager = AuthenticationManager.getInstance();
        boolean isAuthenticated = authenticationManager.authenticateUser("username", "[pass");
        System.out.println("Is authenticated " + isAuthenticated);
    }
}
