from abc import ABC, abstractmethod
from enums.EvictionPolicy import EvictionPolicy
from models.DbInterface import DbInterface  # Assuming this file contains the DbInterface class
from models.CacheObserver import CacheObserver
from typing import List

class Cache(ABC):
    def __init__(self, db_interface, storage, capacity, evictionPolicy, cacheHit, cacheMiss, evictions):
        self.db_interface = db_interface  # HAS-A relationship with DbInterface
        self.storage = {}
        self.evictionPolicy = evictionPolicy
        self.cacheHit = 0
        self.cacheMiss = 0
        self.evictions = 0
        self.capacity = capacity
        self.observers: List[CacheObserver] = []  # List of observers

    def register_observer(self, observer: CacheObserver):
        """
        Register an observer to the cache.
        """
        self.observers.append(observer)

    def unregister_observer(self, observer: CacheObserver):
        """
        Unregister an observer from the cache.
        """
        self.observers.remove(observer)

    def notify_observers(self, action: str, key: str, value: str = None):
        """
        Notify all registered observers about a change in the cache.
        """
        for observer in self.observers:
            observer.notify(action, key, value)

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    def sync_with_db(self, key, value):
        """
        Sync the cache data with the database.
        This is an optional method that can be used to store the cache data in the underlying database.
        :param key: The cache key.
        :param value: The value to be stored in the cache and database.
        """
        self.db_interface.put(key, value)
