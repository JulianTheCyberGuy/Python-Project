# Main Entry Point

from Calc_Module import Calculator
import Utils_Module

def main():
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
        
        # Create an instance of Calculator
        calc = Calculator(num1, num2)

        # Loop to get the correct operation choice
        while invalid_input_count < 3:
            choice = Utils_Module.get_operation_choice()
            try:
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

