import threading
from threading import Lock

# Lazy initialization
class Singleton:
    _instance = None  # Private class variable (equivalent to private static in Java)
    
    def __init__(self):
        # The __init__ method will be called after __new__
        if Singleton._instance is not None:
            raise Exception("This class is a singleton. Use getInstance() method.")
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

class EagerSingleton:
    # Eagerly initialize the singleton instance
    _instance = None

    # Initialize the instance at the time of class definition
    _instance = object.__new__(object)  # Allocate memory for the instance

    def __init__(self):
        if EagerSingleton._instance is not None:
            raise Exception("This class is a singleton. Use get_instance() method.")

    @classmethod
    def get_instance(cls):
        return cls._instance
    


class MultithreadSingleton:
    _instance = None
    _lock = Lock()  # Class level lock for thread synchronization
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            print("Initializing MultithreadSingleton")
            self.initialized = True
    
    @classmethod
    def get_instance(cls):
        # First check (without lock)
        if cls._instance is None:
            # If no instance exists, acquire lock
            with cls._lock:
                # Double check once lock is acquired
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance


# Example usage
if __name__ == "__main__":
    # Lazy initialization test
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()
    print("Lazy Singleton:", s1 is s2)  # True
    
    # This will raise an exception
    try:
        s3 = Singleton()  # Trying to create directly
    except Exception as e:
        print("Exception caught:", str(e))
    
    # Eager initialization test
    obj1 = EagerSingleton.get_instance()
    obj2 = EagerSingleton.get_instance()

    print(obj1 is obj2)  # Output: True

    def get_singleton():
        instance = MultithreadSingleton.get_instance()
        print(f"Instance ID in {threading.current_thread().name}: {id(instance)}")
    
    # Create multiple threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=get_singleton, name=f"Thread-{i+1}")
        threads.append(thread)
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()