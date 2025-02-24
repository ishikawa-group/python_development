# PEP8: Python Style Guide
* PEP8 is a poppular rule for Python coding. It is not mandatory but highly recommended when you write & share your code with others.

### 1. Indentation should be 4 spaces, not tabs.
**Correct**
```python
def my_function():
    print("Hello")
```
**Incorrect**
```python
def my_function():
  print("Hello")  # Two spaces
```

```python
def my_function():
	print("Hello")  # Tab used
```

### 2. Two blank lines before and after functions/classes.
**Correct**
```python
class MyClass:
    pass


def my_function():
    pass
```

### 3. Put whitespace around operators and brackets.
**Correct**
```python
x = 1 + 2  # Space around operators
my_list = [1, 2, 3]  # No extra spaces inside brackets
my_dict = {"key": "value"}  # No space before ':', one after
```
**Incorrect**
```python
x=1+2  # No spaces
my_list = [ 1,2,3 ]  # Extra spaces
my_dict = { "key" :"value" }  # Wrong spacing
```

### 4. Naming Conventions
* Variables & functions: `lower_case_with_underscores`
  **Example:**
  ```python
  user_name = "Alice"
  def calculate_total(): pass
  ```

* Constants (unchanging values): `ALL_CAPS_WITH_UNDERSCORES`
  **Example:**
  ```python
  PI = 3.14159
  MAX_RETRIES = 5
  ```

* Class names: `CamelCase` (each word starts with a capital letter)
  **Example:**
  ```python
  class DataProcessor:
      pass
  ```

* Private variables & methods: Prefix with `_single_underscore`
  **Example:**
  ```python
  class Example:
      def _private_method(self):
        pass
  ```

* Strongly private variables & methods: Prefix with `__double_underscore`
  **Example:**
  ```python
  class Example:
      def __very_private_method(self):
        pass
  ```

* Special methods: `__double_leading_and_trailing_underscores__`
  **Example:**
  ```python
  class Example:
      def __init__(self):
          pass  # Constructor
      def __str__(self):
          return "Example object"  # String representation
  ```

* Modules: `lowercase_with_underscores`
  **Example:**
  ```
  my_module.py
  data_processor.py
  ```

* Packages or libraries: `lowercase-with-hyphens`
  **Example:**
  ```
  numpy
  scikit-learn
  pytorch-lightning
  ```

## Code style other than PEP8
* There are several widely-used code styles other than PEP8.
* One of them is **writing docstring** to a function and class.
* docstring is an explanation for the function and class. There are several doscrtring styles but it is highly recommended to use **Google style**.
```python
def process_data(raw_data, columns=None):
    """
    Do some processing.

    Args:
        raw_data (pandas.DataFrame): raw data
        columns (list, optional): column name list

    Returns:
        pandas.DataFrame: DataFrame after processing.
    """
```

## Exercises

### Exercise 1: Fix Code Style
Fix the following code to comply with PEP8:

```python
class userAccount:
    def __init__ ( self,name,age ):
        self.Name=name
        self.Age=age
    
    def displayInfo(self):
        print(f"Name:{self.Name},Age:{self.Age}")


def Calculate_average( numbers ):
    return sum(numbers)/len(numbers)
```

**Answer:**
```python
class UserAccount:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

Changes made:
- Fixed class name to CamelCase (`UserAccount`)
- Fixed method name to snake_case (`display_info`)
- Fixed function name to snake_case (`calculate_average`)
- Fixed variable names to snake_case (`name`, `age`)
- Added proper spacing around operators and parameters
- Fixed string formatting with spaces after colons

### Exercise 2: Choose Proper Naming Conventions
Choose the appropriate naming convention according to PEP8 for each case:

1. A constant representing maximum database connections
2. A class for processing user data
3. A function for internal use only
4. A module name for reading CSV files
5. A method that returns string representation of an object

**Answer:**
1. `MAX_DB_CONNECTIONS` (uppercase with underscores for constants)
2. `UserDataProcessor` (CamelCase for class names)
3. `_process_internal_data` (single underscore prefix for internal use)
4. `csv_reader.py` (lowercase with underscores for modules)
5. `__str__` (double underscores for special methods)

### Exercise 3: Write a Docstring
Add a Google style docstring to the following function:

```python
def calculate_bmi(weight, height):
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers")
    return weight / (height ** 2)
```

**Answer:**
```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI) from weight and height.

    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters

    Returns:
        float: The calculated BMI value
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers")
    return weight / (height ** 2)
```
