import unittest
from model.tile import Tile
from shared.position import Position

class TileTest(unittest.TestCase):
    def test_moves_tile_above_empty_in_3x3(self):
        self.assertEqual(Tile(Position(0, 1)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3), (1, 0, 3, 4, 2, 5, 6, 7, 8))

    def test_moves_tile_below_empty_in_3x3(self):
        self.assertEqual(Tile(Position(2, 1)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3), (1, 2, 3, 4, 7, 5, 6, 0, 8))

    def test_moves_tile_left_of_empty_in_3x3(self):
        self.assertEqual(Tile(Position(1, 0)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3), (1, 2, 3, 0, 4, 5, 6, 7, 8))

    def test_moves_tile_right_of_empty_in_3x3(self):
        self.assertEqual(Tile(Position(1, 2)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3), (1, 2, 3, 4, 5, 0, 6, 7, 8))

    def test_returns_none_for_diagonal_top_left_to_empty(self):
        self.assertIsNone(Tile(Position(0, 0)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3))

    def test_returns_none_for_diagonal_top_right_to_empty(self):
        self.assertIsNone(Tile(Position(0, 2)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3))

    def test_returns_none_for_diagonal_bottom_left_to_empty(self):
        self.assertIsNone(Tile(Position(2, 0)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3))

    def test_returns_none_for_diagonal_bottom_right_to_empty(self):
        self.assertIsNone(Tile(Position(2, 2)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3))

    def test_returns_none_when_tile_position_equals_empty_position(self):
        self.assertIsNone(Tile(Position(1, 1)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3))

    def test_returns_none_when_tile_is_two_rows_from_empty(self):
        self.assertIsNone(Tile(Position(0, 0)).move((1, 2, 3, 4, 5, 6, 0, 7, 8), 3))

    def test_returns_none_when_tile_is_two_columns_from_empty(self):
        self.assertIsNone(Tile(Position(0, 0)).move((1, 2, 0, 3, 4, 5, 6, 7, 8), 3))

    def test_preserves_source_state_after_move(self):
        state = (1, 2, 3, 4, 0, 5, 6, 7, 8)
        Tile(Position(0, 1)).move(state, 3)
        self.assertEqual(state, (1, 2, 3, 4, 0, 5, 6, 7, 8))

    def test_returns_tuple_type(self):
        self.assertIsInstance(Tile(Position(0, 1)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3), tuple)

    def test_preserves_state_length(self):
        self.assertEqual(len(Tile(Position(0, 1)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3)), 9)

    def test_places_empty_at_target_old_position(self):
        result = Tile(Position(0, 1)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3)
        self.assertEqual(result[1], 0)

    def test_places_target_tile_at_empty_old_position(self):
        result = Tile(Position(0, 1)).move((1, 2, 3, 4, 0, 5, 6, 7, 8), 3)
        self.assertEqual(result[4], 2)

    def test_moves_horizontally_in_2x2(self):
        self.assertEqual(Tile(Position(1, 0)).move((1, 2, 3, 0), 2), (1, 2, 0, 3))

    def test_moves_vertically_in_2x2(self):
        self.assertEqual(Tile(Position(0, 1)).move((1, 2, 3, 0), 2), (1, 0, 3, 2))

    def test_returns_none_for_diagonal_in_2x2(self):
        self.assertIsNone(Tile(Position(0, 0)).move((1, 2, 3, 0), 2))

    def test_moves_in_4x4_with_empty_at_corner(self):
        state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
        self.assertEqual(Tile(Position(2, 3)).move(state, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12))

    def test_moves_in_5x5_with_empty_at_corner(self):
        state = tuple(range(1, 25)) + (0,)
        expected = list(state)
        expected[19], expected[24] = expected[24], expected[19]
        self.assertEqual(Tile(Position(3, 4)).move(state, 5), tuple(expected))

    def test_moves_with_empty_at_top_left_corner(self):
        self.assertEqual(Tile(Position(0, 1)).move((0, 1, 2, 3, 4, 5, 6, 7, 8), 3), (1, 0, 2, 3, 4, 5, 6, 7, 8))

    def test_moves_with_empty_at_top_edge(self):
        self.assertEqual(Tile(Position(1, 1)).move((1, 0, 2, 3, 4, 5, 6, 7, 8), 3), (1, 4, 2, 3, 0, 5, 6, 7, 8))

if __name__ == "__main__":
    unittest.main()
