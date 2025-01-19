from abc import ABC, abstractmethod

class Car:
    @abstractmethod
    def assemble(self) -> None:
        pass

class AbstractFactory(ABC):
    @abstractmethod
    def getCar(self, carType: str) -> Car:
        pass

class ElectricFactory(AbstractFactory):
    def getCar(self, carType: str) -> Car | None:
        if carType == "FORD":
            return ElectricFord()
        return None
    
class PetrolFactory(AbstractFactory):
    def getCar(self, carType: str) -> Car | None:
        if carType == "FORD":
            return PetrolFord()
        return None
    
class ElectricFord(Car):
    def assemble(self) -> None:
        print("Assembling electric ford")

class PetrolFord(Car):
    def assemble(self) -> None:
        print("Assembling petrol ford")

class FactoryProducer:
    @staticmethod
    def getfactory(factory: str) -> AbstractFactory | None:
        if factory == "ELECTRIC":
            return ElectricFactory()
        elif factory == "PETROL":
            return PetrolFactory()
        return None
    
abstractFactory = FactoryProducer.getfactory("PETROL")
abstractFactory.getCar("FORD").assemble()
