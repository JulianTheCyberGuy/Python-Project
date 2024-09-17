import unittest
from Calc_Module import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Setup common resources for tests."""
        self.calc1 = Calculator(10, 5)
        self.calc2 = Calculator(7, 0)
        self.calc3 = Calculator(-4, 9)
    
    # Test for basic operations
    def test_add(self):
        self.assertEqual(self.calc1.add(), 15)
        self.assertEqual(self.calc3.add(), 5)

    def test_subtract(self):
        self.assertEqual(self.calc1.subtract(), 5)
        self.assertEqual(self.calc3.subtract(), -13)

    def test_multiply(self):
        self.assertEqual(self.calc1.multiply(), 50)
        self.assertEqual(self.calc3.multiply(), -36)

    def test_divide(self):
        self.assertEqual(self.calc1.divide(), 2)
        with self.assertRaises(ValueError):
            self.calc2.divide()

    # Test for advanced operations
    def test_exponentiate(self):
        self.assertEqual(self.calc1.exponentiate(), 100000)
        self.assertEqual(self.calc3.exponentiate(), (-4) ** 9)

    def test_modulo(self):
        self.assertEqual(self.calc1.modulo(), 0)
        with self.assertRaises(ValueError):
            self.calc2.modulo()

    def test_sqrt(self):
        self.assertEqual(self.calc1.sqrt(1), 3.1622776601683795)
        self.assertEqual(self.calc1.sqrt(2), 2.23606797749979)
        with self.assertRaises(ValueError):
            self.calc3.sqrt(1)  # negative square root case

    def test_factorial(self):
        # Valid factorial cases
        calc_factorial = Calculator(5, 3)
        self.assertEqual(calc_factorial.factorial(1), 120)  # 5!
        self.assertEqual(calc_factorial.factorial(2), 6)    # 3!

        # Factorial of negative or non-integer should raise ValueError
        with self.assertRaises(ValueError):
            self.calc3.factorial(1)  # factorial of -4
        with self.assertRaises(ValueError):
            Calculator(5.5, 3).factorial(1)  # factorial of non-integer

if __name__ == "__main__":
    unittest.main()
