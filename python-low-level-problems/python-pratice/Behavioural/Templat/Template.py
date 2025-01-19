
from abc import ABC, abstractmethod

# Abstract base class defining the template method
class BeverageMaker(ABC):
    # Template method
    def make_beverage(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()
    
    # Abstract methods to be implemented by subclasses
    @abstractmethod
    def brew(self) -> None:
        pass
    
    @abstractmethod
    def add_condiments(self) -> None:
        pass
    
    # Common methods
    def boil_water(self) -> None:
        print("Boiling water")
    
    def pour_in_cup(self) -> None:
        print("Pouring into cup")

# Concrete implementation for coffee
class CoffeeMaker(BeverageMaker):
    def brew(self) -> None:
        print("Dripping coffee through filter")
    
    def add_condiments(self) -> None:
        print("Adding sugar and milk")

# Concrete implementation for tea
class TeaMaker(BeverageMaker):
    def brew(self) -> None:
        print("Steeping the tea")
    
    def add_condiments(self) -> None:
        print("Adding lemon")

# Client code
def main():
    print("Making tea:")
    tea_maker = TeaMaker()
    tea_maker.make_beverage()
    
    print("\nMaking coffee:")
    coffee_maker = CoffeeMaker()
    coffee_maker.make_beverage()

if __name__ == "__main__":
    main()