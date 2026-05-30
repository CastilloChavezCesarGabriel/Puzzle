from model.heuristic_search import HeuristicSearch
from model.solution import Solution

class HeuristicPuzzleSolver:
    def __init__(self, heuristic):
        self.__heuristic = heuristic

    def solve(self, puzzle):
        return Solution(HeuristicSearch(puzzle, self.__heuristic).run())