# Python Dataclass

The `dataclass` decorator in Python (introduced in Python 3.7) simplifies the creation of classes that are primarily used to store data. It automatically generates several special methods like `__init__`, `__repr__`, and `__eq__`.

## Comparison with Standard Class

### Standard Class Definition
```python
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)
```

### Dataclass Definition
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

Both implementations achieve the same functionality, but the dataclass version:
- Reduces code by ~70%
- Eliminates potential errors in special method implementations
- Maintains better consistency across different data classes
- Makes the code intention clearer (this is a data container)

## Key Features and Benefits

1. **Automatic Method Generation**
   - `__init__`: Constructor
   - `__repr__`: String representation
   - `__eq__`: Equality comparison
   - `__hash__`: (when specified)
   - `__lt__`, `__le__`, `__gt__`, `__ge__`: (when ordered=True)

2. **Type Annotations**
   - Enforces type hints for all fields
   - Improves code readability
   - Enables better IDE support and static type checking

3. **Default Values and Field Customization**
```python
@dataclass
class Configuration:
    host: str = "localhost"  # Default value
    port: int = 8080
    debug: bool = field(default=False, repr=False)  # Hide from repr
```

4. **Immutable Data Structures**
```python
@dataclass(frozen=True)
class Settings:
    api_key: str
    # Attempts to modify will raise FrozenInstanceError
```

## Advanced Features

1. **Post-Init Processing**
```python
@dataclass
class Circle:
    radius: float
    
    def __post_init__(self):
        self.area = 3.14 * self.radius ** 2
```

2. **Inheritance Support**
```python
@dataclass
class Point3D(Point):
    z: int = 0  # Extends Point with z coordinate
```

## Why Choose Dataclass?

1. **Development Speed**
   - Faster to write and maintain
   - Less boilerplate code
   - Reduced chance of errors in special methods

2. **Code Quality**
   - Consistent implementation across the project
   - Built-in type hints support
   - Immutability option for better data integrity

3. **Maintainability**
   - Easier to add/remove fields
   - Clear intention of the class purpose
   - Standard way of handling data classes

4. **Performance**
   - Optimized implementation of special methods
   - No runtime overhead compared to regular classes
   - Efficient memory usage