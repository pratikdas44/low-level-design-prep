package Admin;

public class Main {
    public static void main(String[] args) {
        AdminCommand userMgmtCommand = new UserManagementCommand();
        userMgmtCommand.execute();
    }
}
