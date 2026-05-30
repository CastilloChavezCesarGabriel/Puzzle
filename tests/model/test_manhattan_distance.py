import unittest
from model.manhattan_distance import ManhattanDistance

class ManhattanDistanceTest(unittest.TestCase):
    def test_returns_zero_for_solved_2x2(self):
        self.assertEqual(ManhattanDistance(2).estimate((1, 2, 3, 0)), 0)

    def test_returns_zero_for_solved_3x3(self):
        self.assertEqual(ManhattanDistance(3).estimate((1, 2, 3, 4, 5, 6, 7, 8, 0)), 0)

    def test_returns_zero_for_solved_4x4(self):
        self.assertEqual(ManhattanDistance(4).estimate(tuple(range(1, 16)) + (0,)), 0)

    def test_returns_zero_for_solved_5x5(self):
        self.assertEqual(ManhattanDistance(5).estimate(tuple(range(1, 25)) + (0,)), 0)

    def test_returns_one_when_last_tile_moved_one_position(self):
        self.assertEqual(ManhattanDistance(3).estimate((1, 2, 3, 4, 5, 6, 7, 0, 8)), 1)

    def test_returns_two_when_first_two_tiles_swapped(self):
        self.assertEqual(ManhattanDistance(3).estimate((2, 1, 3, 4, 5, 6, 7, 8, 0)), 2)

    def test_returns_four_when_corner_tiles_swapped_diagonally(self):
        self.assertEqual(ManhattanDistance(3).estimate((5, 2, 3, 4, 1, 6, 7, 8, 0)), 4)

    def test_returns_twelve_when_empty_moves_to_start_in_3x3(self):
        self.assertEqual(ManhattanDistance(3).estimate((0, 1, 2, 3, 4, 5, 6, 7, 8)), 12)

    def test_returns_sixteen_for_reversed_3x3(self):
        self.assertEqual(ManhattanDistance(3).estimate((8, 7, 6, 5, 4, 3, 2, 1, 0)), 16)

    def test_returns_two_for_reversed_2x2(self):
        self.assertEqual(ManhattanDistance(2).estimate((3, 2, 1, 0)), 2)

    def test_returns_six_for_fully_scrambled_2x2(self):
        self.assertEqual(ManhattanDistance(2).estimate((0, 3, 2, 1)), 6)

    def test_returns_one_when_last_two_tiles_swapped_in_2x2(self):
        self.assertEqual(ManhattanDistance(2).estimate((1, 2, 0, 3)), 1)

    def test_returns_one_when_last_two_tiles_swapped_in_4x4(self):
        state = tuple(range(1, 15)) + (0, 15)
        self.assertEqual(ManhattanDistance(4).estimate(state), 1)

    def test_returns_one_when_last_two_tiles_swapped_in_5x5(self):
        state = tuple(range(1, 24)) + (0, 24)
        self.assertEqual(ManhattanDistance(5).estimate(state), 1)

    def test_returns_two_when_two_middle_tiles_swapped_in_4x4(self):
        state = list(range(1, 16)) + [0]
        state[4], state[5] = state[5], state[4]
        self.assertEqual(ManhattanDistance(4).estimate(tuple(state)), 2)

    def test_ignores_empty_tile_when_computing(self):
        self.assertEqual(ManhattanDistance(3).estimate((1, 2, 3, 4, 0, 5, 6, 7, 8)), 6)

    def test_returns_non_negative_for_any_state(self):
        self.assertGreaterEqual(ManhattanDistance(3).estimate((8, 7, 6, 5, 4, 3, 2, 1, 0)), 0)

    def test_distinguishes_different_state_distances(self):
        first = (1, 2, 3, 4, 5, 6, 7, 0, 8)
        second = (1, 2, 3, 4, 0, 5, 6, 7, 8)
        self.assertNotEqual(ManhattanDistance(3).estimate(first), ManhattanDistance(3).estimate(second))

    def test_returns_two_when_one_tile_moved_one_row_in_4x4(self):
        state = list(range(1, 16)) + [0]
        state[4], state[8] = state[8], state[4]
        self.assertEqual(ManhattanDistance(4).estimate(tuple(state)), 2)

    def test_returns_four_for_diagonal_swap_in_4x4(self):
        state = list(range(1, 16)) + [0]
        state[0], state[5] = state[5], state[0]
        self.assertEqual(ManhattanDistance(4).estimate(tuple(state)), 4)

if __name__ == "__main__":
    unittest.main()