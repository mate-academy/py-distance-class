class Distance:

    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float)) -> object:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError(f"Cannot add {type(other)} to Distance")

    def __iadd__(self, other: (int, float)) -> object:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(f"Cannot add {type(other)} to Distance")
        return self

    def __mul__(self, other: (int, float)) -> object:
        if not isinstance(other, (int, float)):
            raise TypeError(
                f"Cannot multiply {type(other)} with {type(self.km)}"
            )
        return Distance(self.km * other)

    def __truediv__(self, other: (int, float)) -> object:
        if not isinstance(other, (int, float)):
            raise TypeError(f"Cannot divide {type(self.km)} by {type(other)}")
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: (int, float)) -> bool:
        return self.km < other

    def __gt__(self, other: (int, float)) -> bool:
        return self.km > other

    def __eq__(self, other: (int, float)) -> bool:
        return self.km == other

    def __le__(self, other: (int, float)) -> bool:
        return self.km <= other

    def __ge__(self, other: (int, float)) -> bool:
        return self.km >= other
