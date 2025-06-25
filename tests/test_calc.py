# tests/test_calculator.py
import unittest
from apit.calc import calculate_apit

class TestCalc(unittest.TestCase):

    def test_calculate_apit(self):
        self.assertEqual(calculate_apit(100000), 0.00)
        self.assertEqual(calculate_apit(150000), 0.00)
        self.assertEqual(calculate_apit(200000), 3000.0)
        self.assertEqual(calculate_apit(250000), 8000.0)
        self.assertEqual(calculate_apit(300000), 18500.0)
        self.assertEqual(calculate_apit(350000), 32500.0)
        self.assertEqual(calculate_apit(400000), 50000.0)
        self.assertEqual(calculate_apit(500000), 86000.0)
        self.assertEqual(calculate_apit(550000), 104000.0)
        self.assertEqual(calculate_apit(1000000), 266000.0)
        self.assertEqual(calculate_apit(1500000), 446000.0)

if __name__ == '__main__':
    unittest.main()
