package mediator.ChatApplication;

public class UserImpl extends User{
    public UserImpl(ChatMediator med, String name){
        super(med, name);
    }

    @Override
    public void send(String msg){
        System.out.println(this.name + " Sending msg = " + msg);
        chatMediator.sendMsg(msg, this);
    }

    @Override
    public void receive(String msg){
        System.out.println(this.name + " Receiving msg = " + msg);
    }
}
