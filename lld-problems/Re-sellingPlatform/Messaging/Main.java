package Messaging;

public class Main {
    public static void main(String[] args) {
        MessagePublisher publisher = new MessagePublisher();
        MessageSubscriber emailSubscriber = new EmailSubscriber();
        MessageSubscriber pushSubscriber = new PushNotificationSubscriber();

        publisher.attach(emailSubscriber);
        publisher.attach(pushSubscriber);

        publisher.notify("New message");
    }
}
