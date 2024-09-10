package observer.HotelManagement;

public class CoffeShop {
    public static void main(String[] args) {
        Customer robert = new Customer("Robert", "French Vanilla");
        Customer bill = new Customer("Bill", "Hot Coffee");

        CoffeAttendant coffeeAttendent = new CoffeAttendant();
        coffeeAttendent.takeOrder(robert);
        coffeeAttendent.takeOrder(bill);

        // prepare drink
        coffeeAttendent.prepareDrink("French Vanilla");
        coffeeAttendent.prepareDrink("Hot Coffee");

        // order up...
        coffeeAttendent.callOutCompletedOrders();
    }
}
