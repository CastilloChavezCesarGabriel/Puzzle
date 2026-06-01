from model.solution import Solution

class PuzzleSolver:
    def __init__(self, heuristic, search_heuristic):
        self.__heuristic = heuristic
        self.__search_algorithm = search_heuristic

    def solve(self, puzzle):
        return Solution(self.__search_algorithm(puzzle, self.__heuristic).run())