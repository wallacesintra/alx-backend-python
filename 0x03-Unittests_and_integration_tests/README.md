# Unittests and Integration Tests

executing test file:

```bash
python -m unittest path/to/test_file.py
```

## Unittest

 focus on individual components or functions in isolation. The goal is to verify that each part of the code works as expected independently. Unit tests are typically fast and cover small pieces of functionality.

## Integration Test

These tests check how different components or systems work together. The goal is to ensure that the interactions between integrated units function correctly. Integration tests are usually slower than unit tests because they involve multiple parts of the system.

## Common Testing Pattern

### Mocking

Mocking is a technique used to replace real objects with mock objects during testing. This is useful when you want to isolate the code being tested from external dependencies.

```python
from unittest.mock import Mock

# Example of mocking a function
mock_function = Mock(return_value=42)
result = mock_function()
assert result == 42
```

### Parametrication

Parametrization allows you to run the same test with different inputs. This is useful for testing a function with a variety of data.

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
])
def test_increment(input, expected):
    assert increment(input) == expected
```

### Fixtures

Fixtures are used to set up and tear down the test environment. They provide a fixed baseline so that tests run reliably and produce consistent results.

```python
import pytest

@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_sample_data(sample_data):
    assert sample_data["key"] == "value"
```
