package mediator.ChatApplication;

public interface ChatMediator {
    public void sendMsg(String msg, User user);
    public void addUser(User user);
}
