from model.heuristic_puzzle_search import HeuristicPuzzleSearch

class HeuristicPuzzleSolver:
    def __init__(self, heuristic):
        self.__heuristic = heuristic

    def solve(self, puzzle):
        return HeuristicPuzzleSearch(puzzle, self.__heuristic).run()