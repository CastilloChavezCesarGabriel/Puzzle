import random
import unittest
from model.iterative_deepening_search import IterativeDeepeningSearch
from model.manhattan_distance import ManhattanDistance
from model.puzzle import Puzzle
from tests.helper.solution_path import SolutionPath

class IterativeDeepeningSearchTest(unittest.TestCase):
    def test_runs_on_already_solved_2x2(self):
        puzzle = Puzzle(2)
        self.assertIsNone(SolutionPath(IterativeDeepeningSearch(puzzle, ManhattanDistance(2)).run()).verify(puzzle))

    def test_runs_on_already_solved_3x3(self):
        puzzle = Puzzle(3)
        self.assertIsNone(SolutionPath(IterativeDeepeningSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_runs_on_already_solved_4x4(self):
        puzzle = Puzzle(4)
        self.assertIsNone(SolutionPath(IterativeDeepeningSearch(puzzle, ManhattanDistance(4)).run()).verify(puzzle))

    def test_runs_on_lightly_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(5)
        self.assertIsNone(SolutionPath(IterativeDeepeningSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_runs_on_moderately_scrambled_3x3(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(10)
        self.assertIsNone(SolutionPath(IterativeDeepeningSearch(puzzle, ManhattanDistance(3)).run()).verify(puzzle))

    def test_runs_on_lightly_scrambled_4x4(self):
        random.seed(0)
        puzzle = Puzzle(4).shuffle(4)
        self.assertIsNone(SolutionPath(IterativeDeepeningSearch(puzzle, ManhattanDistance(4)).run()).verify(puzzle))

    def test_returns_list_type(self):
        solution = IterativeDeepeningSearch(Puzzle(3), ManhattanDistance(3)).run()
        self.assertIsInstance(solution, list)

    def test_returns_single_step_for_already_solved_puzzle(self):
        solution = IterativeDeepeningSearch(Puzzle(3), ManhattanDistance(3)).run()
        self.assertEqual(len(solution), 1)

    def test_first_step_matches_input_puzzle(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(8)
        solution = IterativeDeepeningSearch(puzzle, ManhattanDistance(3)).run()
        self.assertEqual(solution[0], puzzle)

    def test_last_step_is_solved(self):
        random.seed(0)
        puzzle = Puzzle(3).shuffle(8)
        solution = IterativeDeepeningSearch(puzzle, ManhattanDistance(3)).run()
        self.assertTrue(solution[-1].is_solved())

if __name__ == "__main__":
    unittest.main()