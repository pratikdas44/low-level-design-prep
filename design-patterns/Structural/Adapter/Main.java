package design;

public class Main {
    public static void main(String[] args) {
        Vehicle car = new Car();
        car.accelerate();

        Vehicle bicycle = new BicycleAdapter(new Bicycle());
        bicycle.accelerate();
    }
}
