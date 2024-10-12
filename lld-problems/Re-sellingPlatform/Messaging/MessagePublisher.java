package Messaging;

import java.util.ArrayList;
import java.util.List;

public class MessagePublisher {
    private List<MessageSubscriber> subscribers = new ArrayList<>();
    public void attach(MessageSubscriber subscriber){
        subscribers.add(subscriber);
    }

    public void detach(MessageSubscriber subscriber){
        subscribers.remove(subscriber);
    }

    public void notify(String message){
        for(MessageSubscriber subscriber: subscribers){
            subscriber.update(message);
        }
    }
}
