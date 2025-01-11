from enum import Enum

class ConsistencyLevel(Enum):
    CONSISTENT = "consistent"
    EVENTUAL_CONSISTENT = "eventual_consistent"
