package Notifications;

public class Main {
    public static void main(String[] args) {
        NotificationService publisher = new NotificationService();
        NotificationObserver emailSubscriber = new EmailObserver();
        NotificationObserver pushSubscriber = new PushNotificationObserver();

        publisher.attach(emailSubscriber);
        publisher.attach(pushSubscriber);

        publisher.notify("New message");
    }
}
