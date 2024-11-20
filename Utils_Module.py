# Helper module for user interaction functions

def get_number_input(prompt: str) -> float:
    """Prompt user for numeric input and validate it."""
    while True:
        try:
            return float(input(prompt))  # User input is converted to a float
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Handling invalid input with feedback

def get_operation_choice() -> str:
    """Display the list of operations and prompt the user to choose one."""
    print("Select operation:")
    print("1. Add")  # Maps directly to the add() method of Calculator
    print("2. Subtract")  # Maps to subtract()
    print("3. Multiply")  # Maps to multiply()
    print("4. Divide")  # Maps to divide()
    print("5. Exponentiate (num1 ^ num2)")  # Maps to exponentiate()
    print("6. Modulo (num1 % num2)")  # Maps to modulo()
    print("7. Square root (choose 1 for num1 or 2 for num2)")  # Maps to sqrt()
    print("8. Factorial (choose 1 for num1 or 2 for num2)")  # Maps to factorial()
    
    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")  # User input for operation choice
    return choice

def handle_square_root_input() -> int:
    """Prompt user to choose between num1 and num2 for the square root operation."""
    while True:
        try:
            option = int(input("Take square root of (1 for num1, 2 for num2): "))
            if option in [1, 2]:  # Ensuring valid selection
                return option
            else:
                print("Invalid option. Please choose 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def handle_factorial_input() -> int:
    """Prompt user to choose between num1 and num2 for the factorial operation."""
    while True:
        try:
            option = int(input("Take factorial of (1 for num1, 2 for num2): "))
            if option in [1, 2]:  # Ensuring valid selection
                return option
            else:
                print("Invalid option. Please choose 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
