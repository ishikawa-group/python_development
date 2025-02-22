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
