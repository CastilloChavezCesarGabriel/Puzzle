from model.puzzle_cell_visitor import IPuzzleCellVisitor

class PuzzleAssertionVisitor(IPuzzleCellVisitor):
    def __init__(self, expected_state, expected_size):
        self.__expected_state = expected_state
        self.__expected_size = expected_size

    def visit(self, row, column, value):
        index = row * self.__expected_size + column
        expected = self.__expected_state[index]

        if value != expected:
            raise AssertionError(f"cell ({row}, {column}): expected {expected}, got {value}")