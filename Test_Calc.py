import unittest  # Importing the unittest module for creating unit tests
from Calc_Module import Calculator  # Importing the Calculator class from the Calc_Module

# Test class to validate the Calculator class functionality
class TestCalculator(unittest.TestCase):
    # setUp is a special method to prepare common test resources, demonstrating encapsulation.
    def setUp(self):
        """Setup common resources for tests."""
        self.calc1 = Calculator(10, 5)  # Creating Calculator object with initial values
        self.calc2 = Calculator(7, 0)  # Example object to test edge cases
        self.calc3 = Calculator(-4, 9) # Example object with negative values

    # Example of testing the OOP method 'add' for multiple instances
    def test_add(self):
        self.assertEqual(self.calc1.add(), 15)
        self.assertEqual(self.calc3.add(), 5)

    def test_subtract(self):
        self.assertEqual(self.calc1.subtract(), 5)
        self.assertEqual(self.calc3.subtract(), -13)

    def test_multiply(self):
        self.assertEqual(self.calc1.multiply(), 50)
        self.assertEqual(self.calc3.multiply(), -36)

    # Testing the division method, includes handling of exceptions (polymorphism).
    def test_divide(self):
        self.assertEqual(self.calc1.divide(), 2)
        with self.assertRaises(ValueError):  # Ensuring division by zero raises a proper exception
            self.calc2.divide()

    # Test for exponentiation, a method using instance attributes.
    def test_exponentiate(self):
        self.assertEqual(self.calc1.exponentiate(), 100000)
        self.assertEqual(self.calc3.exponentiate(), (-4) ** 9)

    # Test for modulo, shows handling invalid cases (e.g., modulo by zero).
    def test_modulo(self):
        self.assertEqual(self.calc1.modulo(), 0)
        with self.assertRaises(ValueError):
            self.calc2.modulo()

    # Test for square root, demonstrating abstraction with invalid edge case checks.
    def test_sqrt(self):
        self.assertEqual(self.calc1.sqrt(1), 3.1622776601683795)
        self.assertEqual(self.calc1.sqrt(2), 2.23606797749979)
        with self.assertRaises(ValueError):
            self.calc3.sqrt(1)  # Edge case: square root of a negative number

    # Test factorial method; checks invalid inputs and polymorphism of handling types.
    def test_factorial(self):
        calc_factorial = Calculator(5, 3)
        self.assertEqual(calc_factorial.factorial(1), 120)  # 5!
        self.assertEqual(calc_factorial.factorial(2), 6)    # 3!
        
        # Negative and non-integer values must raise exceptions.
        with self.assertRaises(ValueError):
            self.calc3.factorial(1)  # factorial of -4
        with self.assertRaises(ValueError):
            Calculator(5.5, 3).factorial(1)  # factorial of a non-integer

if __name__ == "__main__":
    unittest.main()  # Run all defined test cases
