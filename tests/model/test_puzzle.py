import random
import unittest
from model.manhattan_distance_algorithm import ManhattanDistanceAlgorithm
from model.puzzle import Puzzle
from tests.helper.puzzle_visitor import PuzzleVisitor
from shared.position import Position

class PuzzleTest(unittest.TestCase):
    def test_starts_solved_for_size_2(self):
        self.assertTrue(Puzzle(2).is_solved())

    def test_starts_solved_for_size_3(self):
        self.assertTrue(Puzzle(3).is_solved())

    def test_starts_solved_for_size_4(self):
        self.assertTrue(Puzzle(4).is_solved())

    def test_starts_solved_for_size_5(self):
        self.assertTrue(Puzzle(5).is_solved())

    def test_accepts_custom_state_at_construction(self):
        self.assertFalse(Puzzle(3, (0, 1, 2, 3, 4, 5, 6, 7, 8)).is_solved())

    def test_returns_false_for_scrambled_state(self):
        self.assertFalse(Puzzle(3, (0, 1, 2, 3, 4, 5, 6, 7, 8)).is_solved())

    def test_returns_self_when_moving_a_non_adjacent_tile(self):
        puzzle = Puzzle(3)
        self.assertEqual(puzzle.move(Position(0, 0)), puzzle)

    def test_returns_new_puzzle_when_moving_an_adjacent_tile(self):
        puzzle = Puzzle(3)
        self.assertNotEqual(puzzle.move(Position(1, 2)), puzzle)

    def test_move_preserves_size_in_resulting_puzzle(self):
        moved = Puzzle(3).move(Position(1, 2))
        self.assertNotEqual(moved, Puzzle(4))

    def test_reset_returns_solved_state_after_scramble(self):
        random.seed(0)
        self.assertTrue(Puzzle(3).shuffle(10).reset().is_solved())

    def test_reset_preserves_size_after_scramble(self):
        random.seed(0)
        self.assertEqual(Puzzle(3).shuffle(10).reset(), Puzzle(3))

    def test_reset_from_already_solved_returns_solved(self):
        self.assertTrue(Puzzle(3).reset().is_solved())

    def test_reset_for_size_2(self):
        random.seed(0)
        self.assertEqual(Puzzle(2).shuffle(5).reset(), Puzzle(2))

    def test_reset_for_size_4(self):
        random.seed(0)
        self.assertEqual(Puzzle(4).shuffle(5).reset(), Puzzle(4))

    def test_expand_yields_two_neighbors_from_solved_3x3(self):
        self.assertEqual(len(list(Puzzle(3).expand())), 2)

    def test_expand_yields_two_neighbors_from_solved_4x4(self):
        self.assertEqual(len(list(Puzzle(4).expand())), 2)

    def test_expand_yields_two_neighbors_from_solved_5x5(self):
        self.assertEqual(len(list(Puzzle(5).expand())), 2)

    def test_expand_yields_four_neighbors_from_center_empty(self):
        puzzle = Puzzle(3, (1, 2, 3, 4, 0, 5, 6, 7, 8))
        self.assertEqual(len(list(puzzle.expand())), 4)

    def test_expand_yields_new_puzzle_instances(self):
        for neighbor in Puzzle(3).expand():
            self.assertIsInstance(neighbor, Puzzle)

    def test_returns_zero_when_estimating_solved_state(self):
        self.assertEqual(Puzzle(3).estimate(ManhattanDistanceAlgorithm(3)), 0)

    def test_returns_positive_estimate_for_scrambled_state(self):
        puzzle = Puzzle(3, (0, 1, 2, 3, 4, 5, 6, 7, 8))
        self.assertGreater(puzzle.estimate(ManhattanDistanceAlgorithm(3)), 0)

    def test_forwards_state_and_size_when_accepting_a_visitor(self):
        self.assertIsNone(Puzzle(3).accept(PuzzleVisitor((1, 2, 3, 4, 5, 6, 7, 8, 0), 3)))

    def test_forwards_size_2_when_accepting_a_visitor(self):
        self.assertIsNone(Puzzle(2).accept(PuzzleVisitor((1, 2, 3, 0), 2)))

    def test_forwards_size_4_when_accepting_a_visitor(self):
        self.assertIsNone(Puzzle(4).accept(PuzzleVisitor(tuple(range(1, 16)) + (0,), 4)))

    def test_equates_puzzles_sharing_the_same_state(self):
        self.assertEqual(Puzzle(3), Puzzle(3))

    def test_distinguishes_puzzles_with_different_states(self):
        self.assertNotEqual(Puzzle(3), Puzzle(3, (0, 1, 2, 3, 4, 5, 6, 7, 8)))

    def test_hashes_equal_puzzles_identically(self):
        self.assertEqual(hash(Puzzle(3)), hash(Puzzle(3)))

    def test_shuffle_returns_a_puzzle_instance(self):
        random.seed(0)
        self.assertIsInstance(Puzzle(3).shuffle(10), Puzzle)

if __name__ == "__main__":
    unittest.main()