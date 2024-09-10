package observer.PubSub;

import java.util.ArrayList;
import java.util.List;

public class Publisher {
    List<Subscriber> subscriberList;
    String message;

    public Publisher(){
        this.subscriberList = new ArrayList<>();
    }

    public void addSubscriber(Subscriber subscriber){
        this.subscriberList.add(subscriber);
    }

    public void removeSubscriber(Subscriber subscriber){
        this.subscriberList.remove(subscriber);
    }

    public void notifyUser(String message){
        for(Subscriber subscriber : subscriberList){
            subscriber.update(message);
        }
    }

    public void setMessage(String message){
        this.message = message;
        notifyUser(message);
    }
}
