from typing import List

# Subscriber (Observer) class
class Subscriber:
    def __init__(self, name: str) -> None:
        self._name = name
        self._message: str | None = None
    
    def update(self, message: str) -> None:
        print(f"{self._name} consuming message: {message}")

# Publisher (Subject) class
class Publisher:
    def __init__(self) -> None:
        self._subscribers: List[Subscriber] = []
        self._message: str | None = None
    
    def add_subscriber(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)
    
    def remove_subscriber(self, subscriber: Subscriber) -> None:
        self._subscribers.remove(subscriber)
    
    def notify_users(self, message: str) -> None:
        for subscriber in self._subscribers:
            subscriber.update(message)
    
    def set_message(self, message: str) -> None:
        self._message = message
        self.notify_users(message)

# Client code
def main():
    # Create publisher and subscribers
    topic1 = Publisher()
    subscriber1 = Subscriber("Pratik")
    subscriber2 = Subscriber("PDB")
    
    # Add subscribers to publisher
    topic1.add_subscriber(subscriber1)
    topic1.add_subscriber(subscriber2)
    
    # Set message which will notify all subscribers
    topic1.set_message("Message inserted")

if __name__ == "__main__":
    main()