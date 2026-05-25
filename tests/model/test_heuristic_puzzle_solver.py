import random
import unittest

from model.heuristic_puzzle_solver import HeuristicPuzzleSolver
from model.manhattan_distance_algorithm import ManhattanDistanceAlgorithm
from model.puzzle import Puzzle
from tests.helper.solution_path import SolutionPath
from tests.helper.zero_heuristic import ZeroHeuristic


class HeuristicPuzzleSolverTest(unittest.TestCase):
    def test_solves_already_solved_2x2(self):
        puzzle = Puzzle(2)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(2)).solve(puzzle)).solves(puzzle)

    def test_solves_already_solved_3x3(self):
        puzzle = Puzzle(3)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle)

    def test_solves_already_solved_4x4(self):
        puzzle = Puzzle(4)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(4)).solve(puzzle)).solves(puzzle)

    def test_solves_already_solved_5x5(self):
        puzzle = Puzzle(5)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(5)).solve(puzzle)).solves(puzzle)

    def test_solves_lightly_scrambled_2x2(self):
        random.seed(0)
        puzzle = Puzzle(2).shuffle(3)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(2)).solve(puzzle)).solves(puzzle)

    def test_solves_lightly_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle)

    def test_solves_moderately_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(10)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle)

    def test_solves_heavily_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(20)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle)

    def test_solves_with_alternative_seed_3x3(self):
        random.seed(1)
        puzzle = Puzzle(3).shuffle(10)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle)

    def test_solves_with_third_seed_3x3(self):
        random.seed(2)
        puzzle = Puzzle(3).shuffle(10)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle)

    def test_solves_lightly_scrambled_4x4(self):
        random.seed(0)
        puzzle = Puzzle(4).shuffle(4)
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(4)).solve(puzzle)).solves(puzzle)

    def test_solves_with_zero_heuristic_on_solved_3x3(self):
        puzzle = Puzzle(3)
        SolutionPath(HeuristicPuzzleSolver(ZeroHeuristic(3)).solve(puzzle)).solves(puzzle)

    def test_solves_with_zero_heuristic_on_lightly_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        SolutionPath(HeuristicPuzzleSolver(ZeroHeuristic(3)).solve(puzzle)).solves(puzzle)

    def test_returns_list_type(self):
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(Puzzle(3))
        self.assertIsInstance(solution, list)

    def test_returns_single_step_for_already_solved_puzzle(self):
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(Puzzle(3))
        self.assertEqual(len(solution), 1)

    def test_returns_multi_step_for_scrambled_puzzle(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)
        self.assertGreater(len(solution), 1)

    def test_solution_first_step_matches_input(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(8)
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)
        self.assertEqual(solution[0], puzzle)

    def test_solution_last_step_is_solved(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(8)
        solution = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)
        self.assertTrue(solution[-1].is_solved())

    def test_handles_corner_empty_state(self):
        puzzle = Puzzle(3, (1, 2, 3, 4, 5, 6, 7, 8, 0))
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle)

    def test_handles_edge_empty_state(self):
        puzzle = Puzzle(3, (1, 0, 2, 3, 4, 5, 6, 7, 8))
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle)

    def test_handles_center_empty_state(self):
        puzzle = Puzzle(3, (1, 2, 3, 4, 0, 5, 6, 7, 8))
        SolutionPath(HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(3)).solve(puzzle)).solves(puzzle)


if __name__ == "__main__":
    unittest.main()
