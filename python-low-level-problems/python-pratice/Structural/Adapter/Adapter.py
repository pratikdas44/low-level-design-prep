from abc import ABC, abstractmethod

class Bicycle:
    def go(self) -> None:
        print("using bicycle")

class Vehicle:
    @abstractmethod
    def accelerate(self) -> None:
        pass
    
class Car(Vehicle):
    def accelerate(self) -> None:
        print("Car is acclerating")

class BicycleAdapter(Vehicle):
    def __init__(self, bicycle: 'Bicycle') -> None:
        self._bicycle = bicycle

    def accelerate(self):
        self._bicycle.go()

car = Car()
car.accelerate()

bicycle = BicycleAdapter(Bicycle())
bicycle.accelerate()