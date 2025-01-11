from models.CacheEntry import CacheEntry
from models.Cache import Cache
from enums.ConsistencyLevel import ConsistencyLevel
from enums.EvictionPolicy import EvictionPolicy
from models.CacheObserver import CacheObserver

class DistributedCache(Cache):
    def __init__(self, db_interface, storage, capacity, evictionPolicy, cacheHit, cacheMiss, evictions, nodes, shardMap, replicationFactor, consistencyLevel):
        super().__init__(db_interface, storage, capacity, evictionPolicy, cacheHit, cacheMiss, evictions)
        self.nodes = nodes
        self.shardMap = shardMap
        self.replicationFactor = replicationFactor
        self.consistencyLevel = consistencyLevel

    def _get_shard(self, key):
        shard_id = hash(key) % len(self.nodes)
        return self.shardMap[shard_id]

    def put(self, key, value):
        shard = self._get_shard(key)
        if len(shard) >= self.capacity:
            self.evict(shard)
        
        shard[key] = value
        self.notify_observers("put", key, value)  # Notify observers about the put action
        self._replicate(key, value)

    def get(self, key):
        shard = self._get_shard(key)
        value = shard.get(key, None)
        
        if value:
            self.cacheHit += 1
        else:
            self.cacheMiss += 1

        return value

    def delete(self, key):
        shard = self._get_shard(key)
        if key in shard:
            del shard[key]
            self.evictions += 1
            self.notify_observers("delete", key)  # Notify observers about the delete action

    def evict(self, shard):
        if self.evictionPolicy == EvictionPolicy.LRU:
            pass  # Implement LRU eviction
        elif self.evictionPolicy == EvictionPolicy.FIFO:
            pass  # Implement FIFO eviction
        self.evictions += 1
