package Admin;

public class UserManagementCommand implements AdminCommand{
    @Override
    public void execute(){
        if(checkAuthorization("Admin")){
            System.out.println("User mgmt actions performed");
        } else{
            System.out.println("Unauthorized access");
        }
    }

    public boolean checkAuthorization(String role){
        return role.equals("ADMIN");
    }
}
