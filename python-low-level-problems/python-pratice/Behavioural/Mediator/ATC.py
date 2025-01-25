from abc import ABC, abstractmethod
from typing import List
class ATC(ABC):
    @abstractmethod
    def notify(self, sender, message):
        pass
    @abstractmethod
    def add_user(self, sender):
        pass

class Tower(ATC):
    def __init__(self):
        self.aircrafts: List['Aircraft'] = []

    def add_user(self, sender):
        self.aircrafts.append(sender)

    def notify(self, sender: 'Aircraft', message):
        for aircraft in self.aircrafts:
            if aircraft != sender:
                aircraft.receive_message(message)

class Aircraft(ABC):
    def __init__(self, tower: ATC, name: str):
        self.tower = tower
        self.name = name
        self.tower.add_user(self)
    @abstractmethod
    def send_message(self, msg):
        pass
    @abstractmethod
    def receive_message(self, msg):
        pass

class CommercialPlane(Aircraft):
    def __init__(self, tower, name):
        super().__init__(tower, name)

    def send_message(self, msg):
        print(f"{self.name} Sending msg = {msg}")
        self.tower.notify(self, msg)
    
    def receive_message(self, msg):
        print(f"{self.name} receiving msg = {msg}") 

class PrivateJet(Aircraft):
    def __init__(self, tower, name):
        super().__init__(tower, name)

    def send_message(self, msg):
        print(f"{self.name} Sending msg = {msg}")
        self.tower.notify(self, msg)
    
    def receive_message(self, msg):
        print(f"{self.name} receiving msg = {msg}") 

tower = Tower()
aircraft1 = CommercialPlane(tower, "Flight 1")
aircraft2 = CommercialPlane(tower, "Flight 2")
private_jet = PrivateJet(tower, "Private 1")

aircraft1.send_message("Requesting landing clearance.")
private_jet.send_message("Requesting takeoff clearance.")
aircraft2.send_message("Acknowledging runway clear.")