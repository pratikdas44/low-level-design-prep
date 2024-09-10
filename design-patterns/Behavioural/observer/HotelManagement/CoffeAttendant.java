package observer.HotelManagement;

import java.util.ArrayList;
import java.util.List;

public class CoffeAttendant {
    private List<Customer> customerList;
    private List<String> completedDrinks;

    public CoffeAttendant() {
        customerList = new ArrayList<Customer>();
        completedDrinks = new ArrayList<String>();
    }

    public void takeOrder(Customer customer) {
        this.customerList.add(customer);
        System.out.println("Coffee Attendent: '" + customer.getName()
                + ", I've started working on your order of "
                + customer.getDrinkOrdered() + "'");
    }

    public void prepareDrink(String drinkToBePrepared) {
        this.completedDrinks.add(drinkToBePrepared);
    }

    public void callOutCompletedOrders() {
        for (String readyDrink : completedDrinks) {
            System.out.println("Order up: " + readyDrink);
            for (Customer customer : customerList) {
                customer.orderReady(readyDrink);
            }
        }
    }
}
