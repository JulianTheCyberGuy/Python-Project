# Main Entry Point

from Calc_Module import Calculator
import Utils_Module

def main():
    try:
        # Get inputs for the calculator
        num1 = Utils_Module.get_number_input("Enter the first number: ")
        num2 = Utils_Module.get_number_input("Enter the second number: ")

        # Create an instance of Calculator
        calc = Calculator(num1, num2)

        # Get the user's operation choice
        choice = Utils_Module.get_operation_choice()

        # Perform the selected operation
        if choice == '1':
            print(f"Result: {calc.add()}")
        elif choice == '2':
            print(f"Result: {calc.subtract()}")
        elif choice == '3':
            print(f"Result: {calc.multiply()}")
        elif choice == '4':
            print(f"Result: {calc.divide()}")
        elif choice == '5':
            print(f"Result: {calc.exponentiate()}")
        elif choice == '6':
            print(f"Result: {calc.modulo()}")
        elif choice == '7':
            which_num = Utils_Module.handle_square_root_input()
            print(f"Result: {calc.sqrt(which_num)}")
        elif choice == '8':
            which_num = Utils_Module.handle_factorial_input()
            print(f"Result: {calc.factorial(which_num)}")
        else:
            print("Invalid choice.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
