import unittest
from unittest.mock import patch, call

from src.python.foo import foo


class TestCase(unittest.TestCase):
    def test_foo(self):
        # Prepare
        expected = "Imported greeting: Hello from `bar` and NumPy [1. 1. 1.]"

        # Execute
        actual = foo.build_message()

        # Assert
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
