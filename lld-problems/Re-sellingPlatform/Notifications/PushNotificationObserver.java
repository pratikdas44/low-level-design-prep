package Notifications;

public class PushNotificationObserver implements NotificationObserver{
    @Override
    public void receive(String message){
        System.out.println("PUsh notification received " + message);
    }
}
