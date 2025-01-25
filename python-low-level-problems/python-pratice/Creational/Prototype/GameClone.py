import copy

class Character:
    def __init__(self, name, health, weapon, outfit):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.outfit = outfit

    def clone(self):
        return copy.deepcopy(self)
    
    def customize(self, outfit=None, weapon=None):
        if outfit:
            self.outfit = outfit
        if weapon:
            self.weapon = weapon
        
    def __str__(self):
        return f"Name: {self.name} Health: {self.health} Clone: {self.clone} Weapon: {self.weapon}"
    

ninja = Character(name="Ninja", health=100, weapon="Sword", outfit="Black")
blue_ninja = ninja.clone()
blue_ninja.customize(outfit="Blue",weapon="Bow")

red_ninja = ninja.clone()
red_ninja.customize(outfit="Red")

print(ninja)
print(blue_ninja)
print(red_ninja)