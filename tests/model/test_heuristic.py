import unittest
from model.manhattan_distance import ManhattanDistance
from tests.helper.no_heuristic import NoHeuristic

class HeuristicTest(unittest.TestCase):
    def test_manhattan_distance_inherits_size_2(self):
        self.assertEqual(ManhattanDistance(2).estimate((1, 2, 3, 0)), 0)

    def test_manhattan_distance_inherits_size_3(self):
        self.assertEqual(ManhattanDistance(3).estimate((1, 2, 3, 4, 5, 6, 7, 8, 0)), 0)

    def test_manhattan_distance_inherits_size_4(self):
        self.assertEqual(ManhattanDistance(4).estimate(tuple(range(1, 16)) + (0,)), 0)

    def test_manhattan_distance_inherits_size_5(self):
        self.assertEqual(ManhattanDistance(5).estimate(tuple(range(1, 25)) + (0,)), 0)

    def test_manhattan_distance_inherits_size_6(self):
        self.assertEqual(ManhattanDistance(6).estimate(tuple(range(1, 36)) + (0,)), 0)

    def test_zero_heuristic_inherits_size_2(self):
        self.assertEqual(NoHeuristic(2).estimate((1, 2, 3, 0)), 0)

    def test_zero_heuristic_inherits_size_3(self):
        self.assertEqual(NoHeuristic(3).estimate((1, 2, 3, 4, 5, 6, 7, 8, 0)), 0)

    def test_zero_heuristic_inherits_size_4(self):
        self.assertEqual(NoHeuristic(4).estimate(tuple(range(1, 16)) + (0,)), 0)

    def test_zero_heuristic_inherits_size_5(self):
        self.assertEqual(NoHeuristic(5).estimate(tuple(range(1, 25)) + (0,)), 0)

    def test_zero_heuristic_returns_zero_for_reversed_state(self):
        self.assertEqual(NoHeuristic(3).estimate((8, 7, 6, 5, 4, 3, 2, 1, 0)), 0)

    def test_zero_heuristic_returns_zero_when_empty_at_start(self):
        self.assertEqual(NoHeuristic(3).estimate((0, 1, 2, 3, 4, 5, 6, 7, 8)), 0)

    def test_zero_heuristic_returns_zero_when_empty_at_center(self):
        self.assertEqual(NoHeuristic(3).estimate((1, 2, 3, 4, 0, 5, 6, 7, 8)), 0)

    def test_zero_heuristic_returns_zero_for_scrambled_3x3(self):
        self.assertEqual(NoHeuristic(3).estimate((2, 1, 4, 3, 6, 5, 8, 7, 0)), 0)

    def test_zero_heuristic_returns_zero_for_scrambled_2x2(self):
        self.assertEqual(NoHeuristic(2).estimate((0, 3, 2, 1)), 0)

    def test_manhattan_distance_returns_non_negative_for_any_state(self):
        self.assertGreaterEqual(ManhattanDistance(3).estimate((8, 7, 6, 5, 4, 3, 2, 1, 0)), 0)

    def test_zero_heuristic_returns_non_negative_for_any_state(self):
        self.assertGreaterEqual(NoHeuristic(3).estimate((8, 7, 6, 5, 4, 3, 2, 1, 0)), 0)

    def test_manhattan_distance_returns_one_for_single_tile_off(self):
        self.assertEqual(ManhattanDistance(3).estimate((1, 2, 3, 4, 5, 6, 7, 0, 8)), 1)

    def test_zero_heuristic_returns_zero_even_for_single_tile_off(self):
        self.assertEqual(NoHeuristic(3).estimate((1, 2, 3, 4, 5, 6, 7, 0, 8)), 0)

    def test_concrete_subclasses_share_size_contract(self):
        solved = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.assertEqual(ManhattanDistance(3).estimate(solved), NoHeuristic(3).estimate(solved))

    def test_concrete_subclasses_diverge_on_unsolved_state(self):
        unsolved = (1, 2, 3, 4, 5, 6, 7, 0, 8)
        self.assertNotEqual(ManhattanDistance(3).estimate(unsolved), NoHeuristic(3).estimate(unsolved))

if __name__ == "__main__":
    unittest.main()