from enum import Enum

class EvictionPolicy(Enum):
    LRU = 1
    FIFO = 2
    TTL = 3  # This could be a time-based eviction strategy

