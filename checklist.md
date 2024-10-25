# Check Your Code Against the Following Points

## Make Code Easier

1. **Avoid unnecessary `else` statements:**

**Good example:**

```python
if isinstance(other, (int, float)):
    return "Valid number!"
return "Invalid number!"
```

**Bad example:**

```python
if isinstance(other, (int, float)):
    return "Valid number!"
else:
    return "Invalid number!"
```

## Type Annotations

1. **Use proper type annotations for function arguments and return types:**

**Good example:**
```python
def add_distance(
    dist1: Distance | int | float, 
    dist2: Distance | int | float
) -> Distance:
    return dist1 + dist2
```

**Another good example:**
```python
from typing import Union

def add_distance(
    dist1: Union[Distance, int, float], 
    dist2: Union[Distance, int, float]
) -> Distance:
    return dist1 + dist2
```

**Bad examples:**
```python
def add_distance(
    dist1: "Distance", 
    dist2: (int, float, "Distance")
) -> "Distance":
    return dist1 + dist2
```

2. **Fix `NameError: name 'Distance' is not defined` due to annotations:**

If you encounter a `NameError` due to annotations, you can add the following import at the top of your file:
```python
from __future__ import annotations
```
