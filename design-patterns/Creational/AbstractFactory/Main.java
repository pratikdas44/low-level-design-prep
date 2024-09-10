package AbstractFactory;

public class Main {
    public static void main(String[] args) {
        AbstractFactory factory = FactoryProducer.getFactor("PETROL");
        factory.getCar("FORD").assemble();
    }
}
