public class Milk extends BeverageDecorator{
    public Milk(Beverage beverage){
        super(beverage);
    }

    @Override
    public int getCost(){
        return beverage.getCost() + 5;
    }

    @Override
    public String getDescription(){
        return beverage.getDescription() + "milk ";
    }
}
