from abc import ABC, abstractmethod
from typing import List, Any

# Iterator interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self) -> Any:
        pass

# Container interface
class Container(ABC):
    @abstractmethod
    def get_iterator(self) -> Iterator:
        pass

# Concrete collection
class CollectionOfNames(Container):
    def __init__(self) -> None:
        self._names = [
            "Ashwani Rajput",
            "Soono Jaiswal",
            "Rishi Kumar",
            "Rahul Mehta",
            "Hemant Mishra"
        ]
    
    def get_iterator(self) -> Iterator:
        return self.CollectionOfNamesIterator(self._names)
    
    # Inner iterator class
    class CollectionOfNamesIterator(Iterator):
        def __init__(self, names: List[str]) -> None:
            self._names = names
            self._index = 0
        
        def has_next(self) -> bool:
            return self._index < len(self._names)
        
        def next(self) -> str | None:
            if self.has_next():
                name = self._names[self._index]
                self._index += 1
                return name
            return None

# Client code
def main():
    cmpny_repository = CollectionOfNames()
    iterator = cmpny_repository.get_iterator()
    
    while iterator.has_next():
        name = iterator.next()
        print(f"Name : {name}")

if __name__ == "__main__":
    main()