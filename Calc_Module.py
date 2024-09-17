# Calculator Class

import math

class Calculator:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def add(self) -> float:
        return self.num1 + self.num2

    def subtract(self) -> float:
        return self.num1 - self.num2

    def multiply(self) -> float:
        return self.num1 * self.num2

    def divide(self) -> float:
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return self.num1 / self.num2

    def exponentiate(self) -> float:
        return self.num1 ** self.num2

    def modulo(self) -> float:
        if self.num2 == 0:
            raise ValueError("Cannot perform modulo by zero.")
        return self.num1 % self.num2

    def sqrt(self, which: int = 1) -> float:
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
