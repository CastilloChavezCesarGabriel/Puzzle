from model.puzzle_cell_visitor import IPuzzleCellVisitor

class PuzzleVisitor(IPuzzleCellVisitor):
    def __init__(self, expected_state, expected_size):
        self.__expected_state = expected_state
        self.__expected_size = expected_size

    def visit(self, position, value):
        expected_value = self.__expected_state[position.flatten(self.__expected_size)]
        if value != expected_value:
            raise AssertionError(f"expected {expected_value}, got {value}")
