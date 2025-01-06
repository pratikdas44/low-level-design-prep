# WriteStrategy/Strategy.py
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def write_strategy(self):
        pass
