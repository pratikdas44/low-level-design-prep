package Factory;

public class AnimalFactory {
    public static Animal getAnimal(AnimalType type){
        if(type == AnimalType.CAT){
            return new Cat();
        }
        if(type == AnimalType.DOG){
            return new Dog();
        }
        return null;
    }
}
