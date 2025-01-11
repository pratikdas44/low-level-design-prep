from constants import CellState
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.state = CellState.EMPTY

    def __str__(self):
        return self.state.value


c = Cell(3,3)
print(c)