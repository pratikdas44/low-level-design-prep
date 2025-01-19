# Memento class to store the state
class Memento:
    def __init__(self, height: int, width: int) -> None:
        self._height = height
        self._width = width
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, height: int) -> None:
        self._height = height
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, width: int) -> None:
        self._width = width

# Originator class that creates and restores from mementos
class Originator:
    def __init__(self, height: int, width: int) -> None:
        self._height = height
        self._width = width
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, height: int) -> None:
        self._height = height
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, width: int) -> None:
        self._width = width
    
    def create_memento(self) -> Memento:
        return Memento(self._height, self._width)
    
    def restore_memento(self, memento: Memento) -> None:
        self._height = memento.height
        self._width = memento.width

# Caretaker class that keeps track of multiple mementos
class CareTaker:
    def __init__(self) -> None:
        self._history: list[Memento] = []
    
    def add_memento(self, memento: Memento) -> None:
        self._history.append(memento)
    
    def undo(self) -> Memento | None:
        if self._history:
            return self._history.pop()
        return None

# Client code
def main():
    care_taker = CareTaker()
    originator = Originator(5, 10)
    
    # Create and save first snapshot
    snapshot1 = originator.create_memento()
    care_taker.add_memento(snapshot1)
    
    # Create and save second snapshot
    snapshot2 = originator.create_memento()
    care_taker.add_memento(snapshot2)
    snapshot2.height = 15
    snapshot2.width = 16
    
    # Restore previous state
    restored = care_taker.undo()
    if restored:
        originator.restore_memento(restored)
        
        print(f"Height: {originator.height}, Width: {originator.width}")
        print(f"Height: {restored.height}, Width: {restored.width}")

if __name__ == "__main__":
    main()