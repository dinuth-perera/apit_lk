# tests/test_calculator.py
import unittest
from apit.calc import calculate_apit

class TestCalc(unittest.TestCase):

    def test_calculate_apit(self):
        self.assertEqual(calculate_apit(100000), 0)
        self.assertEqual(calculate_apit(150000), 3500)
        self.assertEqual(calculate_apit(250000), 21000)
        self.assertEqual(calculate_apit(350000), 52500)
        self.assertEqual(calculate_apit(400000), 88500)
        self.assertEqual(calculate_apit(500000), 106500)

if __name__ == '__main__':
    unittest.main()
