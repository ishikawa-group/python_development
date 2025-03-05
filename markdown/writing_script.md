# Writing Python script
* There are two modes to execute the Python program:
  1. Interpreter mode: open up a terminal, and type each lines (after `>>>`).
  2. Script mode: write `sample.py` file and excecute by `python sample.py`.
* For some simple tests, interpreter mode is OK but usually script mode is recommended to do Python programing.
* Using Jupyther Notebook is not recommended, except for very beginners.

## Main function
* When you writing Python script, it is highly recommended to separate **function and class parts** and **main part**.

```python
import somelibrary

def some_function():
    print("This is function")
    return None

if __name__ == __main__:
    print("This is main function")
    ...
    some_function()
    ...
```

### Advantages
* When you execute this script, programs starts with `if __name__ == __main__:` part.
* This is easier to read, because one can start reading code from main function part.
* Other advantage of using `main` function is when `.py` file is read as the *module file*.
  - If there is no `main` function, all the lines are executed when read as a module file. But only non-main part is read when it is used as a module file.

### The other way
* Often it is done to define `main` function and put it in the `if ... main:` part.

```python
def main()
    print("This is main function")

if __name__ == main__:
    main()
```

* Its' your choice to define main function but just `if ... main` is OK.

## Exercises

### 1. Fix the Main Function
* Fix the following code to properly implement the main function structure:

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print("Starting the program")
numbers = [1, 2, 3, 4, 5]
result = calculate_average(numbers)
print(f"The average is: {result}")
```

### Answer

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print("Starting the program")
    numbers = [1, 2, 3, 4, 5]
    result = calculate_average(numbers)
    print(f"The average is: {result}")
```

* Changes made:
  - Added the `if __name__ == "__main__":` part
  - Properly indented the code
  - Added appropriate spacing between functions (two branck lines)

### 2. Module Implementation
* Create a temperature conversion module that can be both imported and run directly. Save it as `temperature.py`:

```python
# Original (needs fixing)
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp = float(input("Enter temperature in Celsius: "))
result = celsius_to_fahrenheit(temp)
print(f"{temp}°C is {result}°F")
```

### Answer

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    temp = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is {result}°F")
```

* Changes made:
  - Added docstrings to functions
  - Added the `if __name__ == "__main__":` part
  - This way, the module can be imported without running the interactive part
