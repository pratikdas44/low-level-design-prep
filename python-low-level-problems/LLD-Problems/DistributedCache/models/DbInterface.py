from abc import ABC, abstractmethod

class DbInterface(ABC):
    @abstractmethod
    def get(self, key):
        """
        Retrieve a value from the database by key.
        :param key: The key to search for in the database.
        :return: The value associated with the key or None if not found.
        """
        pass

    @abstractmethod
    def put(self, key, value):
        """
        Store a value in the database with a given key.
        :param key: The key to store the value under.
        :param value: The value to store.
        """
        pass

    @abstractmethod
    def delete(self, key):
        """
        Delete a value from the database by key.
        :param key: The key to remove from the database.
        """
        pass
