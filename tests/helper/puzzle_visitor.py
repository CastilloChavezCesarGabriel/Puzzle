from model.puzzle_cell_visitor import IPuzzleCellVisitor

class PuzzleVisitor(IPuzzleCellVisitor):
    def __init__(self, expected_state, expected_size):
        self.__expected_state = expected_state
        self.__expected_size = expected_size

    def visit(self, row, column, value):
        expected_value = self.__expected_state[row * self.__expected_size + column]
        if value != expected_value:
            raise AssertionError(f"expected {expected_value}, got {value}")
