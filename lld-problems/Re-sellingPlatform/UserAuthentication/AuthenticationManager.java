package UserAuthentication;

import java.util.HashMap;
import java.util.Map;

public class AuthenticationManager {
    private static AuthenticationManager instance;
    private static Map<String,String> userDetails = new HashMap<>();
    private AuthenticationManager(){
    }

    public static AuthenticationManager getInstance(){
        if(instance == null){
            instance = new AuthenticationManager();
        }
        return instance;
    }

    public void addUser(String username, String password){
        userDetails.put(username, password);
    }

    public boolean authenticateUser(String username, String password){
        return userDetails.containsKey(username) && userDetails.get(username).equals(password);
    }
}
