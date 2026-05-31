import random
import unittest
from model.heuristic_search import HeuristicSearch
from model.manhattan_distance import ManhattanDistance
from model.puzzle import Puzzle
from tests.helper.solution_path import SolutionPath
from tests.helper.no_heuristic import NoHeuristic

class HeuristicPuzzleSearchTest(unittest.TestCase):
    def test_runs_on_already_solved_2x2(self):
        puzzle = Puzzle(2)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(2)).run()).verify(puzzle))

    def test_runs_on_already_solved_3x3(self):
        puzzle = Puzzle(3)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_runs_on_already_solved_4x4(self):
        puzzle = Puzzle(4)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(4)).run()).verify(puzzle))

    def test_runs_on_already_solved_5x5(self):
        puzzle = Puzzle(5)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(5)).run()).verify(puzzle))

    def test_runs_on_lightly_scrambled_2x2(self):
        random.seed(0)
        puzzle = Puzzle(2).shuffle(3)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(2)).run()).verify(puzzle))

    def test_runs_on_lightly_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_runs_on_moderately_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(10)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_runs_on_heavily_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(20)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_runs_with_alternative_seed_3x3(self):
        random.seed(1)
        puzzle = Puzzle(3).shuffle(8)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_runs_with_third_seed_3x3(self):
        random.seed(2)
        puzzle = Puzzle(3).shuffle(8)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_runs_on_lightly_scrambled_4x4(self):
        random.seed(0)
        puzzle = Puzzle(4).shuffle(4)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(4)).run()).verify(puzzle))

    def test_runs_with_zero_heuristic_on_solved_3x3(self):
        puzzle = Puzzle(3)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, NoHeuristic(3)).run()).verify(puzzle))

    def test_runs_with_zero_heuristic_on_lightly_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, NoHeuristic(3)).run()).verify(puzzle))

    def test_returns_list_type(self):
        solution = HeuristicSearch(Puzzle(3), ManhattanDistance(3)).run()
        self.assertIsInstance(solution, list)

    def test_returns_single_step_for_already_solved_puzzle(self):
        solution = HeuristicSearch(Puzzle(3), ManhattanDistance(3)).run()
        self.assertEqual(len(solution), 1)

    def test_returns_multi_step_for_scrambled_puzzle(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        solution = HeuristicSearch(puzzle, ManhattanDistance(3)).run()
        self.assertGreater(len(solution), 1)

    def test_first_step_matches_input_puzzle(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(8)
        solution = HeuristicSearch(puzzle, ManhattanDistance(3)).run()
        self.assertEqual(solution[0], puzzle)

    def test_last_step_is_solved(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(8)
        solution = HeuristicSearch(puzzle, ManhattanDistance(3)).run()
        self.assertTrue(solution[-1].is_solved())

    def test_handles_corner_empty_state(self):
        puzzle = Puzzle(3, (1, 2, 3, 4, 5, 6, 7, 8, 0))
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_handles_edge_empty_state(self):
        puzzle = Puzzle(3, (1, 0, 2, 3, 4, 5, 6, 7, 8))
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_handles_center_empty_state(self):
        puzzle = Puzzle(3, (1, 2, 3, 4, 0, 5, 6, 7, 8))
        self.assertIsNone(SolutionPath(HeuristicSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

if __name__ == "__main__":
    unittest.main()