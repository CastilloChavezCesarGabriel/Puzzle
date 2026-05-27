class PuzzleResetter:
    __MESSAGE = "Reset!"

    def __init__(self, view, duration):
        self.__view = view
        self.__duration = duration

    def reset(self, puzzle):
        new_puzzle = puzzle.reset()
        self.__view.notify(PuzzleResetter.__MESSAGE, self.__duration)
        return new_puzzle