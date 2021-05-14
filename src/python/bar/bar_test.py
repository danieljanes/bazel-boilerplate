import unittest
from src.python.bar import bar

class TestCase(unittest.TestCase):
    def test_bar(self):
        # Prepare
        expected = "Hello from `bar` and NumPy [1. 1. 1.]"

        # Execute
        actual = bar.greeting()

        # Assert
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
