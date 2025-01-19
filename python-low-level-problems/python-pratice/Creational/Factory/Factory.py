from abc import ABC, abstractmethod
from enum import Enum

class Animal(ABC):
    @abstractmethod
    def eat(self) -> None:
        pass

class AnimalType(Enum):
    CAT="CAT"
    DOG="DOG"

class Cat(Animal):
    def eat(self):
        print("Cat is eating")

class Dog(Animal):
    def eat(self):
        print("Dog is eating")


class AnimalFactory:
    @staticmethod
    def get_animal(animal_type: AnimalType):
        match animal_type:
            case AnimalType.CAT:
                return Cat()
            case AnimalType.DOG:
                return Dog()
            case _:
                return None

if __name__ == "__main__":
    animal = AnimalFactory.get_animal(AnimalType.CAT)
    animal.eat()
        