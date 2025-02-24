# Copy and Deepcopy
* In Python, when working with objects and data structures, understanding the difference between shallow copy (`copy`) and deep copy (`deepcopy`) is crucial for managing data effectively and avoiding unexpected behavior in your code.

## Shallow Copy (copy)
* A shallow copy creates a new object but references the same memory addresses for nested objects. This means:
  - Creates a new object at a different memory location
  - References to nested objects remain the same
  - Changes to nested objects in the copy will affect the original
* Example of `copy`
```python
import copy

original_list = [1, [2, 3], {'a': 4}]
shallow_copy = copy.copy(original_list)

# Modifying nested object
shallow_copy[1][0] = 5
print(original_list)  # Output: [1, [5, 3], {'a': 4}]
```
* So, if you change the copy, the original also changes.

## Deep Copy (deepcopy)
* A deep copy creates a new object and recursively copies all nested objects, creating new memory addresses for each level. * This means:
  - Creates a new object at a different memory location
  - Creates new copies of all nested objects
  - Changes to nested objects in the copy won't affect the original
* Example of `deepcopy`
```python
import copy

original_list = [1, [2, 3], {'a': 4}]
deep_copy = copy.deepcopy(original_list)

# Modifying nested object
deep_copy[1][0] = 5
print(original_list)  # Output: [1, [2, 3], {'a': 4}]
```

## When to Use Each
### Use Shallow Copy (copy) when:
- You only need to copy the top-level object
- The object contains only immutable nested objects
- Performance is critical and you understand the implications
- Memory usage is a concern

### Use Deep Copy (deepcopy) when:
- You need a completely independent copy of an object and its nested objects
- You want to ensure modifications to the copy won't affect the original
- Working with complex nested data structures
- Debugging or testing where data isolation is important
