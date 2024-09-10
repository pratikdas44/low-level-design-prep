package AbstractFactory;

public class FactoryProducer {
    public static AbstractFactory getFactor(String factory){
        if(factory.equals("ELECTRIC")){
            return new ElectricFactory();
        }
        else if(factory.equals("PETROL")){
            return new PetrolFactory();
        }
        return null;
    }
}
