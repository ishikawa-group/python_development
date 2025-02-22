# Testing NumPy Arrays with pytest

A concise guide to numpy.testing within pytest framework.

## Essential numpy.testing Functions

```python
import pytest
import numpy as np
from numpy.testing import assert_array_equal, assert_allclose

@pytest.fixture
def test_arrays():
    return {
        'exact': np.array([1, 2, 3]),
        'float': np.array([0.1, 0.2, 0.3])
    }

def test_array_exact(test_arrays):
    """Test exact array equality"""
    result = test_arrays['exact'] * 2
    expected = np.array([2, 4, 6])
    assert_array_equal(result, expected)

def test_array_approximate(test_arrays):
    """Test approximate equality for floating-point calculations"""
    result = test_arrays['float'] * 3
    expected = np.array([0.3, 0.6, 0.9])
    assert_allclose(result, expected, rtol=1e-15)
```

## Key Points

- `assert_array_equal`: Use for exact matching (integers, booleans)
- `assert_allclose`: Use for floating-point comparisons with tolerance
- Fixtures help organize test data
- Run tests with: `pytest -v test_numpy.py`