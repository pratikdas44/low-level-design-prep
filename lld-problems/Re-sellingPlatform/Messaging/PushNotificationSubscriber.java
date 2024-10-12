package Messaging;

public class PushNotificationSubscriber implements MessageSubscriber{
    @Override
    public void update(String message){
        System.out.println("Push notification received " + message);
    }
}