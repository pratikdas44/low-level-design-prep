package Notifications;

public class EmailObserver implements NotificationObserver{
    @Override
    public void receive(String message){
        System.out.println("Email subscriber received " + message);
    }
}
