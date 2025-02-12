class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(
            "Unsupported operand type for +: 'Distance' and '{}'".format(type(other).__name__)
        )

    def __iadd__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                "Unsupported operand type for +=: 'Distance' and '{}'".format(type(other).__name__)
            )
        return self

    def __mul__(self, other: "float | int") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
            "Unsupported operand type for *: 'Distance' and '{}'".format(type(other).__name__)
        )

    def __truediv__(self, other: "float | int") -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError(
                "Unsupported operand type for /: 'Distance' and '{}'".format(type(other).__name__)
            )
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: "Distance | float | int") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return False

    def __lt__(self, other: "Distance | float | int") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: "Distance | float | int") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __le__(self, other: "Distance | float | int") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: "Distance | float | int") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
