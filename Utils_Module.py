# Helper Functions

def get_number_input(prompt: str) -> float:
    """Get and validate numeric input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation_choice() -> str:
    """Display the operation menu and get the user's choice."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate (num1 ^ num2)")
    print("6. Modulo (num1 % num2)")
    print("7. Square root (choose 1 for num1 or 2 for num2)")
    print("8. Factorial (choose 1 for num1 or 2 for num2)")
    
    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")
    return choice

def handle_square_root_input() -> int:
    """Prompt the user to choose between num1 or num2 for the square root."""
    while True:
        try:
            option = int(input("Take square root of (1 for num1, 2 for num2): "))
            if option in [1, 2]:
                return option
            else:
                print("Invalid option. Please choose 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
def handle_factorial_input() -> int:
    """Prompt the user to choose between num1 or num2 for the factorial."""
    while True:
        try:
            option = int(input("Take factorial of (1 for num1, 2 for num2): "))
            if option in [1, 2]:
                return option
            else:
                print("Invalid option. Please choose 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
