package observer.PubSub;

public class Subscriber {
    private String name;
    private String message;

    public Subscriber(String name){
        this.name = name;
    }

    public void update(String message){
        System.out.println("Consuming message " + message);
    }
}
