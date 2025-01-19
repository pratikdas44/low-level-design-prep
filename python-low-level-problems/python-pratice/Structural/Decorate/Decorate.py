from abc import ABC, abstractmethod

# Base interface
class Beverage(ABC):
    @abstractmethod
    def get_cost(self) -> int:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass

# Base decorator
class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage
    
    def get_cost(self) -> int:
        return self._beverage.get_cost()
    
    def get_description(self) -> str:
        return self._beverage.get_description()

# Concrete decorators
class Milk(BeverageDecorator):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)
    
    def get_cost(self) -> int:
        return self._beverage.get_cost() + 5
    
    def get_description(self) -> str:
        return self._beverage.get_description() + "milk "

class Sugar(BeverageDecorator):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)
    
    def get_cost(self) -> int:
        return self._beverage.get_cost() + 1
    
    def get_description(self) -> str:
        return self._beverage.get_description() + "sugar "

# Concrete component
class PlainBeverage(Beverage):
    def get_cost(self) -> int:
        return 5
    
    def get_description(self) -> str:
        return ""

# Usage
def main():
    beverage = Sugar(Milk(PlainBeverage()))
    print(beverage.get_cost())
    print(beverage.get_description())

if __name__ == "__main__":
    main()