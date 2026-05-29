import random
import unittest
from model.heuristic_puzzle_solver import HeuristicPuzzleSolver
from model.manhattan_distance_algorithm import ManhattanDistanceAlgorithm
from model.puzzle import Puzzle
from model.solution import Solution
from tests.helper.solution_path import SolutionPath
from tests.helper.no_heuristic import NoHeuristic

class HeuristicPuzzleSolverTest(unittest.TestCase):
    def test_solves_already_solved_2x2(self):
        puzzle = Puzzle(2)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(2)).solve(puzzle)).solves(puzzle))

    def test_solves_already_solved_3x3(self):
        puzzle = Puzzle(3)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle))

    def test_solves_already_solved_4x4(self):
        puzzle = Puzzle(4)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(4)).solve(puzzle)).solves(puzzle))

    def test_solves_already_solved_5x5(self):
        puzzle = Puzzle(5)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(5)).solve(puzzle)).solves(puzzle))

    def test_solves_lightly_scrambled_2x2(self):
        random.seed(0)
        puzzle = Puzzle(2).shuffle(3)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(2)).solve(puzzle)).solves(puzzle))

    def test_solves_lightly_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle))

    def test_solves_moderately_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(10)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle))

    def test_solves_heavily_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(20)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle))

    def test_solves_with_alternative_seed_3x3(self):
        random.seed(1)
        puzzle = Puzzle(3).shuffle(10)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle))

    def test_solves_with_third_seed_3x3(self):
        random.seed(2)
        puzzle = Puzzle(3).shuffle(10)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle))

    def test_solves_lightly_scrambled_4x4(self):
        random.seed(0)
        puzzle = Puzzle(4).shuffle(4)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(4)).solve(puzzle)).solves(puzzle))

    def test_solves_with_zero_heuristic_on_solved_3x3(self):
        puzzle = Puzzle(3)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(NoHeuristic(3)).solve(puzzle)).solves(puzzle))

    def test_solves_with_zero_heuristic_on_lightly_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(NoHeuristic(3)).solve(puzzle)).solves(puzzle))

    def test_returns_solution_type(self):
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(Puzzle(3))
        self.assertIsInstance(solution, Solution)

    def test_returns_single_step_for_already_solved_puzzle(self):
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(Puzzle(3))
        self.assertEqual(len(list(solution)), 1)

    def test_returns_multi_step_for_scrambled_puzzle(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)
        self.assertGreater(len(list(solution)), 1)

    def test_solution_first_step_matches_input(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(8)
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)
        self.assertEqual(next(iter(solution)), puzzle)

    def test_solution_concludes_solved(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(8)
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)
        self.assertTrue(solution.conclude().is_solved())

    def test_handles_corner_empty_state(self):
        puzzle = Puzzle(3, (1, 2, 3, 4, 5, 6, 7, 8, 0))
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle))

    def test_handles_edge_empty_state(self):
        puzzle = Puzzle(3, (1, 0, 2, 3, 4, 5, 6, 7, 8))
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle))

    def test_handles_center_empty_state(self):
        puzzle = Puzzle(3, (1, 2, 3, 4, 0, 5, 6, 7, 8))
        self.assertIsNone(SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle))

if __name__ == "__main__":
    unittest.main()