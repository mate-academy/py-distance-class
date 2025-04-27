def __add__(self, other: object) -> "Distance":
    if isinstance(other, Distance):
        return Distance(self.km + other.km)
    elif isinstance(other, (int, float)):
        return Distance(self.km + other)
    else:
        raise TypeError(
            f"Unsupported operand type for +: "
            f"'Distance' and '{type(other).__name__}'"
        )

def __iadd__(self, other: object) -> "Distance":
    if isinstance(other, Distance):
        self.km += other.km
    elif isinstance(other, (int, float)):
        self.km += other
    else:
        raise TypeError(
            f"Unsupported operand type for +=: "
            f"'Distance' and '{type(other).__name__}'"
        )
    return self

def __mul__(self, other: float) -> "Distance":
    if isinstance(other, (int, float)):
        return Distance(self.km * other)
    else:
        raise TypeError(
            f"Unsupported operand type for *: "
            f"'Distance' and '{type(other).__name__}'"
        )

def __truediv__(self, other: float) -> "Distance":
    if isinstance(other, (int, float)):
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Distance(self.km / other)
    else:
        raise TypeError(
            f"Unsupported operand type for /: "
            f"'Distance' and '{type(other).__name__}'"
        )

def __lt__(self, other: object) -> bool:
    if isinstance(other, Distance):
        return self.km < other.km
    elif isinstance(other, (int, float)):
        return self.km < other
    else:
        raise TypeError(
            f"Unsupported operand type for <: "
            f"'Distance' and '{type(other).__name__}'"
        )

def __gt__(self, other: object) -> bool:
    if isinstance(other, Distance):
        return self.km > other.km
    elif isinstance(other, (int, float)):
        return self.km > other
    else:
        raise TypeError(
            f"Unsupported operand type for >: "
            f"'Distance' and '{type(other).__name__}'"
        )

def __eq__(self, other: object) -> bool:
    if isinstance(other, Distance):
        return self.km == other.km
    elif isinstance(other, (int, float)):
        return self.km == other
    else:
        raise TypeError(
            f"Unsupported operand type for ==: "
            f"'Distance' and '{type(other).__name__}'"
        )
