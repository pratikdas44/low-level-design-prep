package AbstractFactory;

public class ElectricFactory implements AbstractFactory{
    @Override
    public Car getCar(String type){
        if(type.equals("FORD")) return new ElectricFord();
        return null;
    }
}
