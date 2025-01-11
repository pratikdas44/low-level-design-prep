from enum import Enum

# Enums
class CellState(Enum):
    EMPTY = " "
    X = "X"
    O = "O"

class GameStatus(Enum):
    IN_PROGRESS = "in_progress"
    WIN = "win"
    DRAW = "draw"