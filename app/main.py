class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(
            "Unsupported operand type(s) for +: 'Distance' and "
            f"'{type(other).__name__}'"
        )

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                "Unsupported operand type(s) for +=: 'Distance' and "
                f"'{type(other).__name__}'"
            )
        return self

    def __mul__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
            "Unsupported operand type(s) for *: 'Distance' and "
            f"'{type(other).__name__}'"
        )

    def __truediv__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            result = self.km / other
            return Distance(round(result, 2))
        raise TypeError(
            "Unsupported operand type(s) for /: 'Distance' and "
            f"'{type(other).__name__}'"
        )

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError(
            "'<' not supported between instances of 'Distance' and "
            f"'{type(other).__name__}'"
        )

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        raise TypeError(
            "'>' not supported between instances of 'Distance' and "
            f"'{type(other).__name__}'"
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError(
            "'<=' not supported between instances of 'Distance' and "
            f"'{type(other).__name__}'"
        )

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError(
            "'>=' not supported between instances of 'Distance' and "
            f"'{type(other).__name__}'"
        )
