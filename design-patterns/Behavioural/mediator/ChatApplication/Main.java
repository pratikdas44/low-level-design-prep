package mediator.ChatApplication;

public class Main {
    public static void main(String[] args) {
        ChatMediator chatMediator = new ChatMediatorImpl();
        User user1 = new UserImpl(chatMediator, "A");
        User user2 = new UserImpl(chatMediator, "B");
        User user3 = new UserImpl(chatMediator, "C");
        User user4 = new UserImpl(chatMediator, "D");

        chatMediator.addUser(user1);
        chatMediator.addUser(user2);
        chatMediator.addUser(user3);
        chatMediator.addUser(user4);

        user2.send("Hi there");
    }
}
