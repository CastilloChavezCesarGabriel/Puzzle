from model.heuristic_search import HeuristicSearch
from model.iterative_deepening_search import IterativeDeepeningSearch
from model.manhattan_distance import ManhattanDistance
from model.puzzle_solver import PuzzleSolver

class PuzzleSolverPolicy:
    __ASTAR_MAXIMUM_SIZE = 3

    def create(self, size):
        heuristic = ManhattanDistance(size)
        if size <= self.__ASTAR_MAXIMUM_SIZE:
            return PuzzleSolver(heuristic, HeuristicSearch)
        return PuzzleSolver(heuristic, IterativeDeepeningSearch)