import io
import unittest
from contextlib import redirect_stderr
from model.puzzle_size_validator import PuzzleSizeValidator

class PuzzleSizeValidatorTest(unittest.TestCase):
    def test_accepts_minimum_size(self):
        self.assertIsInstance(PuzzleSizeValidator(2), PuzzleSizeValidator)

    def test_accepts_size_three(self):
        self.assertIsInstance(PuzzleSizeValidator(3), PuzzleSizeValidator)

    def test_accepts_size_four(self):
        self.assertIsInstance(PuzzleSizeValidator(4), PuzzleSizeValidator)

    def test_accepts_size_five(self):
        self.assertIsInstance(PuzzleSizeValidator(5), PuzzleSizeValidator)

    def test_accepts_large_size(self):
        self.assertIsInstance(PuzzleSizeValidator(100), PuzzleSizeValidator)

    def test_rejects_size_one(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleSizeValidator(1)

    def test_rejects_size_zero(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleSizeValidator(0)

    def test_rejects_negative_size(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleSizeValidator(-1)

    def test_rejects_large_negative_size(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                PuzzleSizeValidator(-100)

    def test_error_message_mentions_minimum(self):
        captured = io.StringIO()
        with redirect_stderr(captured):
            with self.assertRaises(SystemExit):
                PuzzleSizeValidator(1)
        self.assertIn("at least 2", captured.getvalue())

    def test_error_message_mentions_actual_value(self):
        captured = io.StringIO()
        with redirect_stderr(captured):
            with self.assertRaises(SystemExit):
                PuzzleSizeValidator(0)
        self.assertIn("0", captured.getvalue())

    def test_error_message_uses_invalid_prefix(self):
        captured = io.StringIO()
        with redirect_stderr(captured):
            with self.assertRaises(SystemExit):
                PuzzleSizeValidator(1)
        self.assertIn("Invalid:", captured.getvalue())

if __name__ == "__main__":
    unittest.main()