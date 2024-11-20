<h1>Calculator Project</h1>

<h2>Overview</h2>
<p>
  This project demonstrates the use of Object-Oriented Programming (OOP) concepts to implement a calculator application.
  The project is modularized into separate files, including a class-based calculator module (<code>Calc_Module.py</code>), 
  a utilities module (<code>Utils_Module.py</code>), and a test suite (<code>Test_Calc.py</code>). 
  The design ensures maintainability, extensibility, and code clarity.
</p>

<h2>Project Structure</h2>
<pre>
project/
├── Calc_Module.py        # Core calculator logic and OOP implementation
├── Utils_Module.py       # Utility functions for user interaction
├── Test_Calc.py          # Unit tests for the calculator functionality
└── README.md             # Documentation for the project
</pre>

<h2>Key OOP Concepts Used</h2>

<h3>1. Encapsulation</h3>
<p>
  The <code>Calculator</code> class in <code>Calc_Module.py</code> encapsulates operations (like addition, multiplication) 
  and the data (operands <code>num1</code>, <code>num2</code>) into a single logical unit. 
  Access to internal details is controlled through methods, ensuring a clean interface.
</p>

<h3>2. Abstraction</h3>
<p>
  The <code>Calculator</code> class provides simple methods like <code>add()</code>, <code>divide()</code>, etc., 
  abstracting the complexity of operations (e.g., handling division by zero or invalid inputs). 
  The user only interacts with the public interface without worrying about implementation details.
</p>

<h3>3. Polymorphism</h3>
<p>
  Methods like <code>divide()</code> and <code>factorial()</code> handle multiple input scenarios gracefully:
  <ul>
      <li>Division by zero raises an exception.</li>
      <li>Factorial rejects invalid inputs like negative or non-integer values.</li>
  </ul>
</p>

<h3>4. Modularity</h3>
<p>
  Each module in the project has a specific responsibility:
  <ul>
      <li><code>Calc_Module.py</code>: Defines the main <code>Calculator</code> class and its methods.</li>
      <li><code>Utils_Module.py</code>: Contains helper functions to handle user inputs and menu interactions.</li>
      <li><code>Test_Calc.py</code>: Tests the <code>Calculator</code> methods to ensure correctness and robustness.</li>
  </ul>
</p>

<h2>Modules Explained</h2>

<h3>1. Calc_Module.py</h3>
<p>
  Contains the <code>Calculator</code> class, which implements:
  <ul>
      <li>Basic operations: <code>add</code>, <code>subtract</code>, <code>multiply</code>, <code>divide</code></li>
      <li>Advanced operations: <code>exponentiate</code>, <code>modulo</code>, <code>sqrt</code>, <code>factorial</code></li>
  </ul>
  Handles invalid input gracefully using exceptions.
</p>

<h3>2. Utils_Module.py</h3>
<p>
  Provides helper functions for:
  <ul>
      <li>Validating numeric input (<code>get_number_input</code>)</li>
      <li>Allowing the user to select operations (<code>get_operation_choice</code>)</li>
      <li>Handling specific inputs for advanced operations like <code>sqrt</code> and <code>factorial</code>.</li>
  </ul>
</p>

<h3>3. Test_Calc.py</h3>
<p>
  Implements unit tests using Python's <code>unittest</code> framework to verify the correctness of the <code>Calculator</code> class methods.
  Ensures all edge cases (e.g., division by zero, negative square roots) are tested.
</p>

<h2>How to Run the Project</h2>

<h3>1. Run the Calculator</h3>
<p>
  Execute the main script (assuming a <code>main.py</code> or equivalent is added later):
</p>
<pre><code>python main.py</code></pre>

<h3>2. Run the Unit Tests</h3>
<p>
  Use the following command to run the test suite:
</p>
<pre><code>python -m unittest Test_Calc.py</code></pre>