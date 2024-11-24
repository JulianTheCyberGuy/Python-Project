import tkinter as tk
from tkinter import messagebox
from Calc_Module import Calculator  # Make sure this module is accessible

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Entry fields for the two numbers
        self.label1 = tk.Label(master, text="Number 1:")
        self.label1.pack()
        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.label2 = tk.Label(master, text="Number 2:")
        self.label2.pack()
        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        # Result label
        self.result_label = tk.Label(master, text="Result:")
        self.result_label.pack()
        self.result = tk.Label(master, text="")
        self.result.pack()

        # Buttons for operations
        self.add_button = tk.Button(master, text="Add", command=self.add)
        self.add_button.pack()

        self.subtract_button = tk.Button(master, text="Subtract", command=self.subtract)
        self.subtract_button.pack()

        self.multiply_button = tk.Button(master, text="Multiply", command=self.multiply)
        self.multiply_button.pack()

        self.divide_button = tk.Button(master, text="Divide", command=self.divide)
        self.divide_button.pack()

        self.exponentiate_button = tk.Button(master, text="Exponentiate", command=self.exponentiate)
        self.exponentiate_button.pack()

        self.modulo_button = tk.Button(master, text="Modulo", command=self.modulo)
        self.modulo_button.pack()

        self.sqrt_button = tk.Button(master, text="Square Root of Number 1", command=self.sqrt)
        self.sqrt_button.pack()

        self.factorial_button = tk.Button(master, text="Factorial of Number 1", command=self.factorial)
        self.factorial_button.pack()

    def get_values(self):
        """Retrieve values from the entry fields and create a Calculator instance."""
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            return Calculator(num1, num2)
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers.")
            return None

    def add(self):
        calc = self.get_values()
        if calc:
            self.result.config(text=str(calc.add()))

    def subtract(self):
        calc = self.get_values()
        if calc:
            self.result.config(text=str(calc.subtract()))

    def multiply(self):
        calc = self.get_values()
        if calc:
            self.result.config(text=str(calc.multiply()))

    def divide(self):
        calc = self.get_values()
        if calc:
            try:
                self.result.config(text=str(calc.divide()))
            except ValueError:
                messagebox.showerror("Math error", "Cannot divide by zero.")

    def exponentiate(self):
        calc = self.get_values()
        if calc:
            self.result.config(text=str(calc.exponentiate()))

    def modulo(self):
        calc = self.get_values()
        if calc:
            try:
                self.result.config(text=str(calc.modulo()))
            except ValueError:
                messagebox.showerror("Math error", "Cannot perform modulo by zero.")

    def sqrt(self):
        calc = self.get_values()
        if calc:
            try:
                self.result.config(text=str(calc.sqrt(1)))  # Using 1 as a dummy argument
            except ValueError:
                messagebox.showerror("Math error", "Cannot take square root of a negative number.")

    def factorial(self):
        calc = self.get_values()
        if calc:
            try:
                self.result.config(text=str(calc.factorial(1)))  # Using 1 as a dummy argument
            except ValueError:
                messagebox.showerror("Math error", "Factorial is not defined for negative numbers or non-integers.")

if __name__ == "__main__":
    root = tk.Tk()
    calculator_gui = CalculatorGUI(root)
    root.mainloop()