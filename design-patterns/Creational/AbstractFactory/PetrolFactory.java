package AbstractFactory;

public class PetrolFactory implements AbstractFactory{
    @Override
    public Car getCar(String type){
        if(type.equals("FORD")) return new PetrolFord();
        return null;
    }
}
