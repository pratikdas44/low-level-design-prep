package Order;

public class Main {
    public static void main(String[] args) {
        Order order = new Order();
        OrderCommand orderCommand = new UpdateOrderStatusCommand(order, "Shipped");
        orderCommand.execute();
        System.out.println("Current order status is :" + order.getStatus());
    }
}
