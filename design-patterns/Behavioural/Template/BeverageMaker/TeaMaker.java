package Template.BeverageMaker;

public class TeaMaker extends BeverageMaker {
    // Implementing abstract methods
    @Override
    void brew() {
        System.out.println("Steeping the tea");
    }
 
    @Override
    void addCondiments() {
        System.out.println("Adding lemon");
    }
}
