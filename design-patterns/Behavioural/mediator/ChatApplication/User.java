package mediator.ChatApplication;

public abstract class User {
    protected ChatMediator chatMediator;
    protected String name;

    public User(ChatMediator med, String name){
        this.chatMediator = med;
        this.name = name;
    }

    public abstract void send(String msg);
    public abstract void receive(String msg);
}
