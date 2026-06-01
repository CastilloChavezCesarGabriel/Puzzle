import unittest
from model.puzzle import Puzzle
from model.puzzle_solver import PuzzleSolver
from model.puzzle_solver_policy import PuzzleSolverPolicy

class PuzzleSolverFactoryTest(unittest.TestCase):
    def test_returns_puzzle_solver_for_size_two(self):
        self.assertIsInstance(PuzzleSolverPolicy().create(2), PuzzleSolver)

    def test_returns_puzzle_solver_for_size_three(self):
        self.assertIsInstance(PuzzleSolverPolicy().create(3), PuzzleSolver)

    def test_returns_puzzle_solver_for_size_four(self):
        self.assertIsInstance(PuzzleSolverPolicy().create(4), PuzzleSolver)

    def test_returns_puzzle_solver_for_size_five(self):
        self.assertIsInstance(PuzzleSolverPolicy().create(5), PuzzleSolver)

    def test_solver_solves_size_two_puzzle(self):
        solver = PuzzleSolverPolicy().create(2)
        self.assertTrue(solver.solve(Puzzle(2)))

    def test_solver_solves_size_four_puzzle(self):
        solver = PuzzleSolverPolicy().create(4)
        self.assertTrue(solver.solve(Puzzle(4)))

if __name__ == "__main__":
    unittest.main()