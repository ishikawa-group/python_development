# Python Abstract Classes
* An abstract class in Python is a class that contains one or more abstract methods. Abstract methods are methods that are declared but don't have an implementation.
* Abstract classes serve as a template for other classes and cannot be instantiated directly.

## Library for abstract classes
* Python provides the `abc` (Abstract Base Classes) module to create abstract classes:

## Advantages of Using Abstract Classes
### 1. Enforced Implementation
* Child classes must implement all abstract methods
* Prevents missing method implementations
* Ensures consistent interface across related classes

### 2. Code Organization
* Provides a clear template for related classes
* Defines a common interface for a group of related classes
* Makes the code more maintainable and structured

### 3. Design Clarity
* Clearly communicates the expected behavior of derived classes
* Makes the code more self-documenting
* Helps in understanding the overall architecture

## Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    # this is abstract class
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    # this is real class
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    # this is real class
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2

# This works
rectangle = Rectangle(5, 3)
circle = Circle(2)

# This raises an error
shape = Shape()  # TypeError: Can't instantiate abstract class
```

## Best Practices
1. Use abstract classes when you want to enforce a common interface across multiple related classes
2. Keep abstract classes focused and cohesive
3. Use clear and descriptive names for abstract methods
4. Document the expected behavior of abstract methods
5. Consider using abstract properties when appropriate

* Abstract classes are particularly useful in large projects where maintaining consistency across multiple implementations is crucial.
* They help in creating more robust and maintainable code by enforcing a clear contract that derived classes must follow.