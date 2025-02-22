# Writing Python script
* There are two modes in Python:
  1. Interpreter mode: open up terminal, and type each lines (after `>>>`).
  2. Script mode: write `sample.py` file and excecute by `python sample.py`.
* For some simple tests, interpreter mode is OK but usually script mode is recommended to do Python programing.
* Using Jupyther Notebook is not recommended, except for very beginners.

## Main function
* When you writing Python script, it is highly recommended to separate **function and class parts** and **main part**.
```python
import some-library

def some_function():
    print("This is function")
    return None

if __name__ == __main__:
  print("This is main function")
  ...
  some_function()
  ...
```
* When you execute this script, programs starts with `if __name__ == __main__:` part.
* This is easier to read, because one can start reading code from main function part.