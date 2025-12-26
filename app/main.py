class Distance:
    def __init__(self: "Distance", km: float) -> None:
        self.km = km

    def __str__(self: "Distance") -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: "Distance") -> str:
        return f"Distance(km={self.km})"

    def __add__(self: "Distance", other: object) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError(
                f"Unsupported operand type for +: "
                f"'Distance' and '{type(other).__name__}'"
            )

    def __iadd__(self: "Distance", other: object) -> "Distance":
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

    def __mul__(self: "Distance", other: float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError(
                f"Unsupported operand type for *: "
                f"'Distance' and '{type(other).__name__}'"
            )

    def __truediv__(self, other: float) -> "Distance":
    if not isinstance(other, (int, float)):
        raise TypeError(
            f"Unsupported operand type for /: "
            f"'Distance' and '{type(other).__name__}'"
        )
    if other == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return Distance(self.km / other)

    def __lt__(self: "Distance", other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError(
                f"Unsupported operand type for <: "
                f"'Distance' and '{type(other).__name__}'"
            )

    def __gt__(self: "Distance", other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError(
                f"Unsupported operand type for >: "
                f"'Distance' and '{type(other).__name__}'"
            )

    def __eq__(self: "Distance", other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError(
                f"Unsupported operand type for ==: "
                f"'Distance' and '{type(other).__name__}'"
            )

    def __le__(self: "Distance", other: object) -> bool:
        return self < other or self == other

    def __ge__(self: "Distance", other: object) -> bool:
        return self > other or self == other
