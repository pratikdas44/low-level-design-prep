from abc import ABC, abstractmethod

# Strategy interface
class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> None:
        pass

# Concrete strategies
class Addition(Strategy):
    def execute(self, a: int, b: int) -> None:
        print(a + b)

class Subtraction(Strategy):
    def execute(self, a: int, b: int) -> None:
        print(a - b)

# Context
class Context:
    def __init__(self) -> None:
        self._strategy: Strategy | None = None
    
    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def execute(self, a: int, b: int) -> None:
        if self._strategy is None:
            raise ValueError("Strategy not set")
        self._strategy.execute(a, b)

# Client code
def main():
    context = Context()
    context.set_strategy(Addition())
    context.execute(2, 3)  # Outputs: 5
    
    # Can switch strategy at runtime
    context.set_strategy(Subtraction())
    context.execute(2, 3)  # Outputs: -1

if __name__ == "__main__":
    main()