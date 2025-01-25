'''ctrl+shift+p ->  type copilot -> select copilot generate test '''
import unittest
from inlineSuggestions import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_average_of_positive_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)

    def test_average_of_negative_numbers(self):
        self.assertEqual(calculate_average([-1, -2, -3, -4, -5]), -3)

    def test_average_of_mixed_numbers(self):
        self.assertEqual(calculate_average([-1, 0, 1]), 0)

    def test_average_of_single_number(self):
        self.assertEqual(calculate_average([10]), 10)

    def test_average_of_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_average([])

if __name__ == '__main__':
    unittest.main()