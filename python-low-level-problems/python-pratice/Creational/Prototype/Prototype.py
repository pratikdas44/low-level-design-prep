from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def clone(self):
        pass

class Rectangle(Shape):
    def __init__(self, w: int, h: int):
        super().__init__(w, h)  # Call parent class constructor
    
    def draw(self) -> None:
        print("Rectangle")
    
    def clone(self) -> Shape:
        return Rectangle(self.width, self.height)

class Square(Shape):
    def __init__(self, w: int, h: int):
        super().__init__(w, h)  # Call parent class constructor
    
    def draw(self) -> None:
        print("Square")
    
    def clone(self) -> Shape:
        return Square(self.width, self.height)
    
if __name__ == "__main__":
    square = Square(10,5)
    square.draw()
    squareClone = square.clone()
    squareClone.draw()


    