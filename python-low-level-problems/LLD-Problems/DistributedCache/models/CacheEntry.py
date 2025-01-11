import time

class CacheEntry:
    def __init__(self, data, ttl):
        """
        Initialize the CacheEntry object with the data, timestamp, TTL, and hit count.
        
        :param data: The data to be stored in the cache.
        :param ttl: The Time-To-Live for the cache entry, in seconds.
        """
        self.data = data               # The actual data stored in the cache
        self.timestamp = time.time()    # The timestamp when the entry was created/added
        self.ttl = ttl                 # Time-To-Live (TTL) for the cache entry
        self.hitCount = 0              # Number of times the cache entry has been accessed

    def is_expired(self):
        """
        Check if the cache entry has expired based on its TTL.
        
        :return: True if the entry is expired, False otherwise.
        """
        return (time.time() - self.timestamp) > self.ttl

    def increment_hit_count(self):
        """
        Increment the hit count when the cache entry is accessed.
        """
        self.hitCount += 1
