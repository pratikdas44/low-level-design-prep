from abc import ABC, abstractmethod

class Person:
    def __init__(self, builder: 'Person.PersonBuilder') -> None:
        self._name = builder.name
        self._university = builder.university
        self._age = builder.age

    def __str__(self) -> str:
        return f"{self._name} {self._university} {self._age}"

    
    class PersonBuilder:
        def __init__(self, name: str, university: str, age: int) -> None:
            self.name = name
            self.university = university
            self.age = age

        def build(self) -> 'Person':
            return Person(self)
        
person = Person.PersonBuilder("John", "MIT", 25).build()
print(person) 