from abc import ABC, abstractmethod
from typing import List

# Mediator interface
class ChatMediator(ABC):
    @abstractmethod
    def send_msg(self, msg: str, user: 'User') -> None:
        pass
    
    @abstractmethod
    def add_user(self, user: 'User') -> None:
        pass

# Concrete mediator
class ChatMediatorImpl(ChatMediator):
    def __init__(self) -> None:
        self._users: List[User] = []
    
    def add_user(self, user: 'User') -> None:
        self._users.append(user)
    
    def send_msg(self, msg: str, user: 'User') -> None:
        for u in self._users:
            if u != user:
                u.receive(msg)

# Abstract user
class User(ABC):
    def __init__(self, med: ChatMediator, name: str) -> None:
        self._mediator = med
        self._name = name
    
    @abstractmethod
    def send(self, msg: str) -> None:
        pass
    
    @abstractmethod
    def receive(self, msg: str) -> None:
        pass

# Concrete user
class UserImpl(User):
    def __init__(self, med: ChatMediator, name: str) -> None:
        super().__init__(med, name)
    
    def send(self, msg: str) -> None:
        print(f"{self._name} Sending msg = {msg}")
        self._mediator.send_msg(msg, self)
    
    def receive(self, msg: str) -> None:
        print(f"{self._name} Receiving msg = {msg}")

# Client code
def main():
    chat_mediator = ChatMediatorImpl()
    
    user1 = UserImpl(chat_mediator, "A")
    user2 = UserImpl(chat_mediator, "B")
    user3 = UserImpl(chat_mediator, "C")
    user4 = UserImpl(chat_mediator, "D")
    
    chat_mediator.add_user(user1)
    chat_mediator.add_user(user2)
    chat_mediator.add_user(user3)
    chat_mediator.add_user(user4)
    
    user2.send("Hi there")

if __name__ == "__main__":
    main()