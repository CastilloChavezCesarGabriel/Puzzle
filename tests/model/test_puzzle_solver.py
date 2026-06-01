import random
import unittest
from model.heuristic_search import HeuristicSearch
from model.iterative_deepening_search import IterativeDeepeningSearch
from model.manhattan_distance import ManhattanDistance
from model.puzzle import Puzzle
from model.puzzle_solver import PuzzleSolver
from model.solution import Solution
from tests.helper.solution_path import SolutionPath

class PuzzleSolverTest(unittest.TestCase):
    def test_solves_with_astar_on_solved_3x3(self):
        puzzle = Puzzle(3)
        solver = PuzzleSolver(ManhattanDistance(3), HeuristicSearch)
        self.assertIsNone(SolutionPath(solver.solve(puzzle)).verify(puzzle))

    def test_solves_with_astar_on_lightly_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        solver = PuzzleSolver(ManhattanDistance(3), HeuristicSearch)
        self.assertIsNone(SolutionPath(solver.solve(puzzle)).verify(puzzle))

    def test_solves_with_idastar_on_solved_3x3(self):
        puzzle = Puzzle(3)
        solver = PuzzleSolver(ManhattanDistance(3), IterativeDeepeningSearch)
        self.assertIsNone(SolutionPath(solver.solve(puzzle)).verify(puzzle))

    def test_solves_with_idastar_on_lightly_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        solver = PuzzleSolver(ManhattanDistance(3), IterativeDeepeningSearch)
        self.assertIsNone(SolutionPath(solver.solve(puzzle)).verify(puzzle))

    def test_solves_with_idastar_on_solved_4x4(self):
        puzzle = Puzzle(4)
        solver = PuzzleSolver(ManhattanDistance(4), IterativeDeepeningSearch)
        self.assertIsNone(SolutionPath(solver.solve(puzzle)).verify(puzzle))

    def test_returns_solution_type_with_astar(self):
        solution = PuzzleSolver(ManhattanDistance(3), HeuristicSearch).solve(Puzzle(3))
        self.assertIsInstance(solution, Solution)

    def test_returns_solution_type_with_idastar(self):
        solution = PuzzleSolver(ManhattanDistance(3), IterativeDeepeningSearch).solve(Puzzle(3))
        self.assertIsInstance(solution, Solution)

if __name__ == "__main__":
    unittest.main()