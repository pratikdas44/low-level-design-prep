from abc import ABC, abstractmethod
from collections import OrderedDict
import time

class EvictionStrategy(ABC):
    @abstractmethod
    def evict(self, cache_data):
        """Evict one or more items from the cache based on the eviction strategy"""
        pass

class LRU(EvictionStrategy):
    def evict(self, cache_data):
        """Evict the least recently used item"""
        if cache_data:
            # Remove the least recently used item, which is the first item in the ordered dict
            return cache_data.popitem(last=False)
        return None

class FIFO(EvictionStrategy):
    def evict(self, cache_data):
        """Evict the first inserted item"""
        if cache_data:
            # Remove the first inserted item, which is the first item in the ordered dict
            return cache_data.popitem(last=False)
        return None

class TTL(EvictionStrategy):
    def __init__(self, ttl):
        self.ttl = ttl  # TTL in seconds

    def evict(self, cache_data):
        """Evict items that have exceeded their TTL"""
        current_time = time.time()
        to_evict = []
        
        # Check which entries are expired
        for key, (value, timestamp) in cache_data.items():
            if current_time - timestamp > self.ttl:
                to_evict.append(key)
        
        # Evict expired entries
        for key in to_evict:
            del cache_data[key]
        
        return to_evict
