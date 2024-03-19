# test_calculator.py

from calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    """Pruebas para la clase Calculator."""

    def test_add(self):
        """Test para el método add."""
        self.assertEqual(Calculator.add(1, 2), 3)

    def test_subtract(self):
        """Test para el método subtract."""
        self.assertEqual(Calculator.subtract(4, 2), 2)

if __name__ == '__main__':
    unittest.main()
