package observer.PubSub;

public class Client {
    public static void main(String[] args) {
        Publisher topic1 = new Publisher();
        Subscriber subscriber1 = new Subscriber("Pratik");
        Subscriber subscriber2 = new Subscriber("PDB");

        topic1.addSubscriber(subscriber1);
        topic1.addSubscriber(subscriber2);

        topic1.setMessage("Message inserted");
    }
}
