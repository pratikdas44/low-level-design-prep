from abc import ABC, abstractmethod
from typing import List, Union

# Visitor interface
class ShoppingCartVisitor(ABC):
    @abstractmethod
    def visit_book(self, book: 'Book') -> int:
        pass
    
    @abstractmethod
    def visit_fruit(self, fruit: 'Fruit') -> int:
        pass

# Element interface
class ItemElement(ABC):
    @abstractmethod
    def accept(self, visitor: ShoppingCartVisitor) -> int:
        pass

# Concrete elements
class Book(ItemElement):
    def __init__(self, price: int, isbn: str) -> None:
        self._price = price
        self._isbn_number = isbn
    
    @property
    def price(self) -> int:
        return self._price
    
    @property
    def isbn_number(self) -> str:
        return self._isbn_number
    
    def accept(self, visitor: ShoppingCartVisitor) -> int:
        return visitor.visit_book(self)

class Fruit(ItemElement):
    def __init__(self, price_per_kg: int, weight: int, name: str) -> None:
        self._price_per_kg = price_per_kg
        self._weight = weight
        self._name = name
    
    @property
    def price_per_kg(self) -> int:
        return self._price_per_kg
    
    @property
    def weight(self) -> int:
        return self._weight
    
    @property
    def name(self) -> str:
        return self._name
    
    def accept(self, visitor: ShoppingCartVisitor) -> int:
        return visitor.visit_fruit(self)

# Concrete visitor
class ShoppingCartVisitorImpl(ShoppingCartVisitor):
    def visit_book(self, book: Book) -> int:
        cost = 0
        # Apply 5$ discount if book price is greater than 50
        if book.price > 50:
            cost = book.price - 5
        else:
            cost = book.price
        
        print(f"Book ISBN::{book.isbn_number} cost = {cost}")
        return cost
    
    def visit_fruit(self, fruit: Fruit) -> int:
        cost = fruit.price_per_kg * fruit.weight
        print(f"{fruit.name} cost = {cost}")
        return cost

# Helper function to calculate total price
def calculate_price(items: List[ItemElement]) -> int:
    visitor = ShoppingCartVisitorImpl()
    return sum(item.accept(visitor) for item in items)

# Client code
def main():
    items = [
        Book(20, "1234"),
        Book(100, "5678"),
        Fruit(10, 2, "Banana"),
        Fruit(5, 5, "Apple")
    ]
    
    total = calculate_price(items)
    print(f"Total Cost = {total}")

if __name__ == "__main__":
    main()