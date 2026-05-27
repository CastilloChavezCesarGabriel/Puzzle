from model.heuristic_puzzle_search import HeuristicPuzzleSearch
from model.solution import Solution

class HeuristicPuzzleSolver:
    def __init__(self, heuristic):
        self.__heuristic = heuristic

    def solve(self, puzzle):
        return Solution(HeuristicPuzzleSearch(puzzle, self.__heuristic).run())