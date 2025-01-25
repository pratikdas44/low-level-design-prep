from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_individual(self, individual: 'Customer') -> int:
        pass

    @abstractmethod
    def visit_org(self, organization: 'Organization') -> int:
        pass

class Client(ABC):
    @abstractmethod
    def accept(self, visitor: 'Visitor') -> int:
        pass
    
class Customer(Client):
    def __init__(self, income):
        self.income = income

    def accept(self, visitor: 'Visitor'):
        return visitor.visit_individual(self)

class Organization(Client):
    def __init__(self, revenue):
        self.revenue = revenue

    
    def accept(self, visitor: 'Visitor'):
        return visitor.visit_org(self)

class TaxCalculator(Visitor):
    def visit_individual(self, individual):
        tax = individual.income * 0.15
        print(f"Individual tax is {tax:.2f}")
        return tax

    def visit_org(self, organization):
        tax = organization.revenue * 0.30
        print(f"Corporate tax is {tax:.2f}")
        return tax

taxCalc = TaxCalculator()
items = [
        Customer(500000),
        Organization(10000),
        Organization(30000),
        Customer(20000)
    ]

def calculate(items):
    return sum(item.accept(taxCalc) for item in items)


print(calculate(items))