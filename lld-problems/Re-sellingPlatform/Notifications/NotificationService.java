package Notifications;
import java.util.ArrayList;
import java.util.List;

public class NotificationService {
    private List<NotificationObserver> subscribers = new ArrayList<>();
    public void attach(NotificationObserver subscriber){
        subscribers.add(subscriber);
    }

    public void detach(NotificationObserver subscriber){
        subscribers.remove(subscriber);
    }

    public void notify(String message){
        for(NotificationObserver subscriber: subscribers){
            subscriber.receive(message);
        }
    }
}
