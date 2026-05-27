class PuzzleMover:
    __SOLVED_MESSAGE = "Solved!"

    def __init__(self, view, duration):
        self.__view = view
        self.__duration = duration

    def move(self, puzzle, position):
        new_puzzle = puzzle.move(position)
        if new_puzzle != puzzle and new_puzzle.is_solved():
            self.__view.notify(PuzzleMover.__SOLVED_MESSAGE, self.__duration)
        return new_puzzle