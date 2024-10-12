package Messaging;

public class EmailSubscriber implements MessageSubscriber{
    @Override
    public void update(String message){
        System.out.println("Email subscriber received " + message);
    }
}
