# Main Entry Point

from Calc_Module import Calculator  # Import the Calculator class
import Utils_Module  # Utility module for helper functions (not provided)

def main():
    """
    Main function: Entry point of the program.
    Demonstrates the usage of the Calculator class to perform various operations.
    """

    invalid_input_count = 0  # Counter for invalid inputs
    
    try:
        # Loop to get the correct inputs from the user
        while invalid_input_count < 3:
            try:
                # Get inputs for the calculator
                num1 = Utils_Module.get_number_input("Enter the first number: ")
                num2 = Utils_Module.get_number_input("Enter the second number: ")
                break  # If inputs are valid, break the loop
            except ValueError:
                invalid_input_count += 1
                print(f"Invalid input. {3 - invalid_input_count} attempts left.")
        
        if invalid_input_count >= 3:
            print("Stop Wasting My Time User")
            return  # Exit the program after 3 failed attempts

        # Reset invalid input counter for operations
        invalid_input_count = 0
        
        # Create an instance of Calculator (object creation: key OOP concept)
        calc = Calculator(num1, num2)

        # Loop to get the correct operation choice
        while invalid_input_count < 3:
            choice = Utils_Module.get_operation_choice()
            try:
                # Perform the selected operation
                if choice == '1':
                    print(f"Result: {calc.add()}")  # Calls add method
                elif choice == '2':
                    print(f"Result: {calc.subtract()}")  # Calls subtract method
                elif choice == '3':
                    print(f"Result: {calc.multiply()}")  # Calls multiply method
                elif choice == '4':
                    print(f"Result: {calc.divide()}")  # Calls divide method
                elif choice == '5':
                    print(f"Result: {calc.exponentiate()}")  # Calls exponentiate method
                elif choice == '6':
                    print(f"Result: {calc.modulo()}")  # Calls modulo method
                elif choice == '7':
                    which_num = Utils_Module.handle_square_root_input()
                    print(f"Result: {calc.sqrt(which_num)}")  # Calls sqrt method
                elif choice == '8':
                    which_num = Utils_Module.handle_factorial_input()
                    print(f"Result: {calc.factorial(which_num)}")  # Calls factorial method
                else:
                    raise ValueError("Invalid operation choice.")
                break  # If the operation choice is valid, break the loop
            except ValueError as e:
                invalid_input_count += 1
                print(f"{e}. {3 - invalid_input_count} attempts left.")
        
        if invalid_input_count >= 3:
            print("Stop Wasting My Time User")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

