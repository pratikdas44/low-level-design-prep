from abc import ABC, abstractmethod

class VegetableMenu(ABC):
    def cook(self):
        self.cut_veggies()
        self.add_ingredients()
        self.cooking_time()
        self.eat()

    @abstractmethod
    def add_ingredients(self):
        pass

    @abstractmethod
    def cut_veggies(self):
        pass

    def cooking_time(self):
        print("Cooking time is 15 mins")
    
    def eat(self):
        print("Eating")

class PaneerDish(VegetableMenu):
    def cut_veggies(self):
        print("Cutting paneer")

    def add_ingredients(self):
        print("Adding paneer masala")

class AlooDish(VegetableMenu):
    def cut_veggies(self):
        print("Cutting aloo")

    def add_ingredients(self):
        print("Adding dum masala")

paneer = PaneerDish()
paneer.cook()

aloo = AlooDish()
aloo.cook()