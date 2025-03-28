package observer.HotelManagement;

public class Customer {
    public String name;
    public String drinkOrdered;

    public Customer(String name, String drinkOrdered){
        this.name = name;
        this.drinkOrdered = drinkOrdered;
    }

    public String getName(){
        return this.name;
    }

    public String getDrinkOrdered(){
        return this.drinkOrdered;
    }

    public void orderReady(String completedDrink){
        if(drinkOrdered.equals(completedDrink)){
            exitStore();
        }
    }

    private void exitStore() {
        System.out.println(name + ": Thank you, I've recieved my "
                + drinkOrdered + " and leaving the store now...");
    }

}
