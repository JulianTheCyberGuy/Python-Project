# Calculator Class

import math

class Calculator:
    """
    This class represents a Calculator.
    It encapsulates functionality for basic arithmetic and advanced calculations.
    """

    def __init__(self, num1: float, num2: float):
        """
        Constructor method: Initializes the Calculator object with two numbers.
        Demonstrates encapsulation by storing state (num1, num2) within the object.
        """
        self.num1 = num1  # First number
        self.num2 = num2  # Second number

    def add(self) -> float:
        """
        Method to perform addition. Demonstrates the behavior of the object.
        """
        return self.num1 + self.num2

    def subtract(self) -> float:
        """
        Method to perform subtraction.
        """
        return self.num1 - self.num2

    def multiply(self) -> float:
        """
        Method to perform multiplication.
        """
        return self.num1 * self.num2

    def divide(self) -> float:
        """
        Method to perform division. Includes error handling (a form of encapsulation)
        to ensure safe operation (e.g., avoiding division by zero).
        """
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return self.num1 / self.num2

    def exponentiate(self) -> float:
        """
        Method to perform exponentiation (num1 raised to the power of num2).
        """
        return self.num1 ** self.num2

    def modulo(self) -> float:
        """
        Method to calculate the remainder of num1 divided by num2.
        Includes error handling for modulo by zero.
        """
        if self.num2 == 0:
            raise ValueError("Cannot perform modulo by zero.")
        return self.num1 % self.num2

    def sqrt(self, which: int = 1) -> float:
        """
        Method to calculate the square root of num1 or num2.
        Uses the `which` parameter to determine which number to use.
        """
        if which == 1:
            if self.num1 < 0:
                raise ValueError("Cannot take the square root of a negative number.")
            return math.sqrt(self.num1)
        elif which == 2:
            if self.num2 < 0:
                raise ValueError("Cannot take the square root of a negative number.")
            return math.sqrt(self.num2)
        else:
            raise ValueError("Invalid option for square root.")

    def factorial(self, which: int = 1) -> int:
        """
        Method to calculate the factorial of num1 or num2.
        Factorial is only defined for non-negative integers, and this is enforced.
        """
        if which == 1:
            if self.num1 < 0 or not self.num1.is_integer():
                raise ValueError("Factorial is only defined for non-negative integers.")
            return math.factorial(int(self.num1))
        elif which == 2:
            if self.num2 < 0 or not self.num2.is_integer():
                raise ValueError("Factorial is only defined for non-negative integers.")
            return math.factorial(int(self.num2))
        else:
            raise ValueError("Invalid option for factorial.")
