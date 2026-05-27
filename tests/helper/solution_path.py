class SolutionPath:
    def __init__(self, steps):
        self.__steps = list(steps)

    def solves(self, input_puzzle):
        if self.__steps[0] != input_puzzle:
            raise AssertionError("solution does not start at the input puzzle")
        if not self.__steps[-1].is_solved():
            raise AssertionError("solution does not end in a solved state")
        for step in range(len(self.__steps) - 1):
            if self.__steps[step + 1] not in list(self.__steps[step].expand()):
                raise AssertionError(f"invalid move at step {step + 1}")