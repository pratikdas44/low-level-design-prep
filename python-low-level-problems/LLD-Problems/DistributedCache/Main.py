from models.DistributedCache import DistributedCache 
from models.CacheObserver import CacheLogger
from models.DbInterface import DbInterface
from enums.EvictionPolicy import EvictionPolicy

db_interface = DbInterface()  # Assuming DbInterface is implemented
storage = {}  # Your storage (e.g., dictionary)
capacity = 1000  # Cache capacity
evictionPolicy = EvictionPolicy.LRU  # Example eviction policy
cacheHit = 0
cacheMiss = 0
evictions = 0
nodes = []  # List of nodes
shardMap = {}  # Map of shard IDs to storage locations
replicationFactor = 2
consistencyLevel = "strong"

# Create the DistributedCache instance
distributed_cache = DistributedCache(
    db_interface, 
    storage, 
    capacity, 
    evictionPolicy, 
    cacheHit, 
    cacheMiss, 
    evictions, 
    nodes, 
    shardMap, 
    replicationFactor, 
    consistencyLevel
)

# Create a logger observer
cache_logger = CacheLogger()

# Register the observer
distributed_cache.register_observer(cache_logger)

# Perform some cache operations
distributed_cache.put("key1", "value1")
distributed_cache.get("key1")
distributed_cache.delete("key1")

# Unregister the observer
distributed_cache.unregister_observer(cache_logger)

