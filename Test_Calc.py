import unittest  # Importing unittest framework for structured test cases
from Calc_Module import Calculator  # Importing the Calculator class to be tested


# Test class for validating Calculator object behavior
class TestCalculator(unittest.TestCase):

    # setUp runs before each test method
    # Demonstrates encapsulation by preparing reusable Calculator objects
    def setUp(self):
        self.calc1 = Calculator(10, 5)   # Standard positive values
        self.calc2 = Calculator(7, 0)    # Used for division/modulo by zero edge cases
        self.calc3 = Calculator(-4, 9)   # Used for negative-value edge cases

    # Test addition method across multiple Calculator instances
    def test_add(self):
        self.assertEqual(self.calc1.add(), 15)
        self.assertEqual(self.calc3.add(), 5)
        # Ensure internal object state is updated correctly
        self.assertEqual(self.calc1.get_last_result(), 15)

    # Test subtraction behavior and internal state tracking
    def test_subtract(self):
        self.assertEqual(self.calc1.subtract(), 5)
        self.assertEqual(self.calc3.subtract(), -13)
        self.assertEqual(self.calc1.get_last_result(), 5)

    # Test multiplication operation and persistence of last_result
    def test_multiply(self):
        self.assertEqual(self.calc1.multiply(), 50)
        self.assertEqual(self.calc3.multiply(), -36)
        self.assertEqual(self.calc1.get_last_result(), 50)

    # Test division, including exception handling for division by zero
    def test_divide(self):
        self.assertEqual(self.calc1.divide(), 2)
        self.assertEqual(self.calc1.get_last_result(), 2)
        # Ensure invalid division raises an exception
        with self.assertRaises(ValueError):
            self.calc2.divide()

    # Test exponentiation using instance attributes
    def test_exponentiate(self):
        self.assertEqual(self.calc1.exponentiate(), 100000)
        self.assertEqual(self.calc3.exponentiate(), (-4) ** 9)
        self.assertEqual(self.calc1.get_last_result(), 100000)

    # Test modulo operation and error handling for modulo by zero
    def test_modulo(self):
        self.assertEqual(self.calc1.modulo(), 0)
        self.assertEqual(self.calc1.get_last_result(), 0)
        with self.assertRaises(ValueError):
            self.calc2.modulo()

    # Test square root operations using explicit object behavior methods
    def test_sqrt(self):
        # Square root of num1 for calc1 (sqrt(10))
        self.assertEqual(self.calc1.sqrt_num1(), 3.1622776601683795)

        # Square root of num2 for calc1 (sqrt(5))
        self.assertEqual(self.calc1.sqrt_num2(), 2.23606797749979)

        # Square root of a negative number should raise an exception
        with self.assertRaises(ValueError):
            self.calc3.sqrt_num1()

    # Test factorial methods and validation of invalid inputs
    def test_factorial(self):
        calc_factorial = Calculator(5, 3)

        # Valid factorial calculations
        self.assertEqual(calc_factorial.factorial_num1(), 120)  # 5!
        self.assertEqual(calc_factorial.factorial_num2(), 6)    # 3!

        # Factorial of a negative number should raise an exception
        with self.assertRaises(ValueError):
            self.calc3.factorial_num1()

        # Factorial of a non-integer should raise an exception
        with self.assertRaises(ValueError):
            Calculator(5.5, 3).factorial_num1()


# Entry point for running the test suite
if __name__ == "__main__":
    unittest.main()