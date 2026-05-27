class PuzzleShuffler:
    __MESSAGE = "Shuffled!"
    __STEPS = 40

    def __init__(self, view, duration):
        self.__view = view
        self.__duration = duration

    def shuffle(self, puzzle):
        new_puzzle = puzzle.shuffle(PuzzleShuffler.__STEPS)
        self.__view.notify(PuzzleShuffler.__MESSAGE, self.__duration)
        return new_puzzle