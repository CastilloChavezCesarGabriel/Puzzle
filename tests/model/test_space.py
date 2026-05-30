import unittest
from model.space import Space

class SpaceTest(unittest.TestCase):
    def test_yields_two_neighbors_when_empty_at_top_left_in_3x3(self):
        self.assertEqual(len(Space((0, 1, 2, 3, 4, 5, 6, 7, 8), 3).expand()), 2)

    def test_yields_two_neighbors_when_empty_at_top_right_in_3x3(self):
        self.assertEqual(len(Space((1, 2, 0, 3, 4, 5, 6, 7, 8), 3).expand()), 2)

    def test_yields_two_neighbors_when_empty_at_bottom_left_in_3x3(self):
        self.assertEqual(len(Space((1, 2, 3, 4, 5, 6, 0, 7, 8), 3).expand()), 2)

    def test_yields_two_neighbors_when_empty_at_bottom_right_in_3x3(self):
        self.assertEqual(len(Space((1, 2, 3, 4, 5, 6, 7, 8, 0), 3).expand()), 2)

    def test_yields_three_neighbors_when_empty_on_top_edge_in_3x3(self):
        self.assertEqual(len(Space((1, 0, 2, 3, 4, 5, 6, 7, 8), 3).expand()), 3)

    def test_yields_three_neighbors_when_empty_on_bottom_edge_in_3x3(self):
        self.assertEqual(len(Space((1, 2, 3, 4, 5, 6, 7, 0, 8), 3).expand()), 3)

    def test_yields_three_neighbors_when_empty_on_left_edge_in_3x3(self):
        self.assertEqual(len(Space((1, 2, 3, 0, 4, 5, 6, 7, 8), 3).expand()), 3)

    def test_yields_three_neighbors_when_empty_on_right_edge_in_3x3(self):
        self.assertEqual(len(Space((1, 2, 3, 4, 5, 0, 6, 7, 8), 3).expand()), 3)

    def test_yields_four_neighbors_when_empty_at_center_in_3x3(self):
        self.assertEqual(len(Space((1, 2, 3, 4, 0, 5, 6, 7, 8), 3).expand()), 4)

    def test_each_neighbor_is_one_step_from_center_empty(self):
        empty = 4
        for neighbor in Space((1, 2, 3, 4, 0, 5, 6, 7, 8), 3).expand():
            row_distance = abs(empty // 3 - neighbor // 3)
            column_distance = abs(empty % 3 - neighbor % 3)
            self.assertEqual(row_distance + column_distance, 1)

    def test_yields_two_neighbors_for_2x2_corner(self):
        self.assertEqual(len(Space((1, 2, 3, 0), 2).expand()), 2)

    def test_yields_two_neighbors_for_4x4_corner(self):
        state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
        self.assertEqual(len(Space(state, 4).expand()), 2)

    def test_yields_two_neighbors_for_5x5_corner(self):
        state = tuple(range(1, 25)) + (0,)
        self.assertEqual(len(Space(state, 5).expand()), 2)

    def test_yields_four_neighbors_when_empty_at_center_in_4x4(self):
        state = (1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertEqual(len(Space(state, 4).expand()), 4)

    def test_yields_four_neighbors_when_empty_at_center_in_5x5(self):
        state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
        self.assertEqual(len(Space(state, 5).expand()), 4)

    def test_returns_list_type(self):
        self.assertIsInstance(Space((1, 2, 3, 4, 0, 5, 6, 7, 8), 3).expand(), list)

    def test_all_neighbors_within_bounds_in_3x3(self):
        for neighbor in Space((1, 2, 3, 4, 0, 5, 6, 7, 8), 3).expand():
            self.assertTrue(0 <= neighbor < 9)

    def test_neighbors_are_distinct_when_empty_at_center(self):
        neighbors = Space((1, 2, 3, 4, 0, 5, 6, 7, 8), 3).expand()
        self.assertEqual(len(set(neighbors)), len(neighbors))

    def test_center_neighbors_cover_all_four_directions(self):
        self.assertEqual(sorted(Space((1, 2, 3, 4, 0, 5, 6, 7, 8), 3).expand()), [1, 3, 5, 7])

    def test_top_edge_neighbors_exclude_above(self):
        self.assertEqual(sorted(Space((1, 0, 2, 3, 4, 5, 6, 7, 8), 3).expand()), [0, 2, 4])

    def test_left_edge_neighbors_exclude_left(self):
        self.assertEqual(sorted(Space((1, 2, 3, 0, 4, 5, 6, 7, 8), 3).expand()), [0, 4, 6])

if __name__ == "__main__":
    unittest.main()