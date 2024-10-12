package Order;

public class UpdateOrderStatusCommand implements OrderCommand{
    private Order order;
    private String newStatus;

    public UpdateOrderStatusCommand(Order order, String newStatus){
        this.order = order;
        this.newStatus = newStatus;
    }

    @Override
    public void execute(){
        order.setStatus(newStatus);
        System.out.println("Order status updated to " + newStatus);
    }
}
