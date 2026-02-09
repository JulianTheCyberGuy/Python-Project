import math

class Calculator:
    """
    Calculator object that encapsulates operands, behavior,
    and internal calculation state.
    """

    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2
        self.last_result = None  # Persistent object state

    # ---- Basic Operations ----

    def add(self) -> float:
        self.last_result = self.num1 + self.num2
        return self.last_result

    def subtract(self) -> float:
        self.last_result = self.num1 - self.num2
        return self.last_result

    def multiply(self) -> float:
        self.last_result = self.num1 * self.num2
        return self.last_result

    def divide(self) -> float:
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero.")
        self.last_result = self.num1 / self.num2
        return self.last_result

    def exponentiate(self) -> float:
        self.last_result = self.num1 ** self.num2
        return self.last_result

    def modulo(self) -> float:
        if self.num2 == 0:
            raise ValueError("Cannot perform modulo by zero.")
        self.last_result = self.num1 % self.num2
        return self.last_result

    # ---- Advanced Operations (Explicit, OOP-Friendly) ----

    def sqrt_num1(self) -> float:
        if self.num1 < 0:
            raise ValueError("Cannot take square root of a negative number.")
        self.last_result = math.sqrt(self.num1)
        return self.last_result

    def sqrt_num2(self) -> float:
        if self.num2 < 0:
            raise ValueError("Cannot take square root of a negative number.")
        self.last_result = math.sqrt(self.num2)
        return self.last_result

    def factorial_num1(self) -> int:
        if self.num1 < 0 or not float(self.num1).is_integer():
            raise ValueError("Factorial is only defined for non-negative integers.")
        self.last_result = math.factorial(int(self.num1))
        return self.last_result

    def factorial_num2(self) -> int:
        if self.num2 < 0 or not float(self.num2).is_integer():
            raise ValueError("Factorial is only defined for non-negative integers.")
        self.last_result = math.factorial(int(self.num2))
        return self.last_result

    # ---- State-Oriented Behavior ----

    def get_last_result(self):
        """Expose internal state safely."""
        return self.last_result

    def clear(self):
        """Reset calculator state."""
        self.last_result = None
