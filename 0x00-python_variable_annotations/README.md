# Type Annotation

Type annotations in Python allow you to specify the expected data types of variables, function parameters, and return values.

```python
age: int = 25
```

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Ducking Typing

"Duck typing" is a concept in Python that means an object's suitability for a task is determined by the presence of certain methods and properties, rather than the actual type of the object.

## Mypy

installation:

```bash
pip install mypy
```

usage:

```bash
mypy your_script.py
```
