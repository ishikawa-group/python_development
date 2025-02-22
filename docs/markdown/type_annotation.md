# Type Annotation in Python

Type annotation in Python is a feature that allows developers to add type hints to variables, function parameters, and return values. Introduced in Python 3.5, it helps improve code readability and enables better tooling support.

## Key Features

- Optional: Python remains dynamically typed
- Helps catch type-related bugs early through static type checkers like mypy
- Enhances code documentation and IDE support
- Can be used with the typing module for complex types
- Improves code maintainability and refactoring

## Basic Syntax

```python
# Variable annotation
name: str = "John"
age: int = 30

# Function annotation
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

## Advanced Type Hints

### Union Types
```python
from typing import Union

# Variable can be either string or int
value: Union[str, int] = "42"
value = 42  # Also valid

# Function accepting multiple types
def process_data(data: Union[str, int, float]) -> str:
    return str(data)
```

### Optional Types
```python
from typing import Optional

# Parameter that might be None
def get_user(user_id: Optional[int] = None) -> str:
    if user_id is None:
        return "Anonymous"
    return f"User {user_id}"
```

### Type Aliases
```python
from typing import Dict, List

# Creating type aliases for complex types
UserID = int
Scores = Dict[str, int]
Matrix = List[List[float]]

def process_scores(user: UserID, scores: Scores) -> Matrix:
    # Implementation here
    pass
```

### Generic Types
```python
from typing import TypeVar, List

T = TypeVar('T')

def first_element(lst: List[T]) -> T:
    if lst:
        return lst[0]
    raise ValueError("Empty list")
```

## Real-world Example

```python
from typing import Dict, List, Optional, Union

class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

class Database:
    def get_user(self, user_id: int) -> Optional[User]:
        # Might return None if user not found
        pass

    def search_users(
        self,
        criteria: Dict[str, Union[str, int]],
        limit: Optional[int] = None
    ) -> List[User]:
        # Returns list of users matching criteria
        pass
```

Type annotations are particularly useful in:
- Large codebases with multiple developers
- APIs and library development
- Complex data processing applications
- Projects requiring high reliability and maintainability