# Type annotations in Python functions
## Introduction

* Type annotations were introduced in Python 3.5 (PEP 484) to provide optional static typing. They allow developers to specify expected types for variables, function arguments, and return values. * While Python remains a dynamically typed language, type annotations help with:
  - Code documentation
  - IDE support and tooling
  - Static type checking (using tools like mypy)
  - Better code maintainability

## Basic syntax
* Type annotations use a colon (`:`) for arguments and an arrow (`->`) for return types:

```python
def function_name(argument: type) -> return_type:
    pass
```

## Return type annotations
* The primary use of type annotations is to specify return types:

```python
def calculate_sum() -> int:
    return 1 + 2

def get_name() -> str:
    return "Alice"

def is_valid() -> bool:
    return True
```

## Argument type annotations
* While the focus is on return types, you can also annotate arguments when needed:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def multiply(x: int, y: int) -> int:
    return x * y
```

## Note
* While argument type annotations are available, focusing on return type annotations often provides the most value for code maintainability and documentation.
