class PuzzleVisitor:
    def __init__(self, expected_state, expected_size):
        self.__expected_state = expected_state
        self.__expected_size = expected_size

    def visit(self, state, size):
        if state != self.__expected_state:
            raise AssertionError(f"expected state {self.__expected_state}, got {state}")
        if size != self.__expected_size:
            raise AssertionError(f"expected size {self.__expected_size}, got {size}")