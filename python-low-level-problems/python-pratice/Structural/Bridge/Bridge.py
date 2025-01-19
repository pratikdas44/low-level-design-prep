from abc import ABC, abstractmethod

class BreatheImplementor:
    @abstractmethod
    def breathe(self) -> None:
        pass

class LandBreatheImplementor(BreatheImplementor):
    def breathe(self):
        print("breathe in land")

class WaterBreatheImplementor(BreatheImplementor):
    def breathe(self):
        print("breathe in water")

class LivingThings(ABC):
    def __init__(self, breatheImplementor: BreatheImplementor):
        self.breatheImplementor = breatheImplementor
    
    @abstractmethod
    def breathingProcess():
        pass

class Dog(LivingThings):
    def __init__(self, breatheImplementor: BreatheImplementor):
        super().__init__(breatheImplementor)

    def breathingProcess(self):
        self.breatheImplementor.breathe()

class Fish(LivingThings):
    def __init__(self, breatheImplementor: BreatheImplementor):
        super().__init__(breatheImplementor)

    def breathingProcess(self):
        self.breatheImplementor.breathe()

fish = Fish(WaterBreatheImplementor())
fish.breathingProcess()
