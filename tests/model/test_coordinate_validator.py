import io
import unittest
from contextlib import redirect_stderr
from model.coordinate_validator import CoordinateValidator

class CoordinateValidatorTest(unittest.TestCase):
    def test_accepts_zero(self):
        self.assertIsInstance(CoordinateValidator(0), CoordinateValidator)

    def test_accepts_one(self):
        self.assertIsInstance(CoordinateValidator(1), CoordinateValidator)

    def test_accepts_positive_value(self):
        self.assertIsInstance(CoordinateValidator(7), CoordinateValidator)

    def test_accepts_large_positive_value(self):
        self.assertIsInstance(CoordinateValidator(1000), CoordinateValidator)

    def test_rejects_negative_one(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                CoordinateValidator(-1)

    def test_rejects_negative_large_value(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                CoordinateValidator(-100)

    def test_error_message_mentions_non_negative(self):
        captured = io.StringIO()
        with redirect_stderr(captured):
            with self.assertRaises(SystemExit):
                CoordinateValidator(-1)
        self.assertIn("non-negative", captured.getvalue())

    def test_error_message_mentions_actual_value(self):
        captured = io.StringIO()
        with redirect_stderr(captured):
            with self.assertRaises(SystemExit):
                CoordinateValidator(-5)
        self.assertIn("-5", captured.getvalue())

if __name__ == "__main__":
    unittest.main()
