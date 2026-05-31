import io
import unittest
from contextlib import redirect_stderr
from model.puzzle_state_validator import PuzzleStateValidator

class PuzzleStateValidatorTest(unittest.TestCase):
    def test_accepts_none_state(self):
        self.assertIsInstance(PuzzleStateValidator(None, 3), PuzzleStateValidator)

    def test_accepts_none_state_for_size_two(self):
        self.assertIsInstance(PuzzleStateValidator(None, 2), PuzzleStateValidator)

    def test_accepts_solved_state_for_size_two(self):
        self.assertIsInstance(PuzzleStateValidator((1, 2, 3, 0), 2), PuzzleStateValidator)

    def test_accepts_solved_state_for_size_three(self):
        self.assertIsInstance(PuzzleStateValidator((1, 2, 3, 4, 5, 6, 7, 8, 0), 3), PuzzleStateValidator)

    def test_accepts_scrambled_state_for_size_three(self):
        self.assertIsInstance(PuzzleStateValidator((0, 1, 2, 3, 4, 5, 6, 7, 8), 3), PuzzleStateValidator)

    def test_accepts_state_with_empty_first(self):
        self.assertIsInstance(PuzzleStateValidator((0, 1, 2, 3), 2), PuzzleStateValidator)

    def test_accepts_state_for_size_four(self):
        state = tuple(range(1, 16)) + (0,)
        self.assertIsInstance(PuzzleStateValidator(state, 4), PuzzleStateValidator)

    def test_rejects_state_with_wrong_length(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleStateValidator((1, 2, 3), 2)

    def test_rejects_state_too_short(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleStateValidator((1, 2, 0), 2)

    def test_rejects_state_too_long(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleStateValidator((1, 2, 3, 4, 0), 2)

    def test_rejects_state_missing_zero(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleStateValidator((1, 2, 3, 4), 2)

    def test_rejects_state_with_duplicates(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleStateValidator((1, 2, 2, 0), 2)

    def test_rejects_state_with_out_of_range_values(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleStateValidator((1, 2, 3, 5), 2)

    def test_rejects_state_with_negative_values(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleStateValidator((-1, 1, 2, 3), 2)

    def test_rejects_state_with_all_zeros(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleStateValidator((0, 0, 0, 0), 2)

    def test_error_message_mentions_size(self):
        captured = io.StringIO()
        with redirect_stderr(captured):
            with self.assertRaises(SystemExit):
                PuzzleStateValidator((1, 2), 2)
        self.assertIn("2", captured.getvalue())

if __name__ == "__main__":
    unittest.main()
