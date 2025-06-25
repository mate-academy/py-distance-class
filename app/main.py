class Distance:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            other = other.km
        return Distance(km=self.km + other)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            other = other.km
        self.km += other
        return self

    def __mul__(self, other: (int, float)) -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError(
                "__mul__ only supports multiplication by int or float"
            )
        return Distance(km=self.km * other)

    def __truediv__(self, other: (int, float)) -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError(
                "__truediv__ only supports division by int or float"
            )
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km < other

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km > other

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km == other

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km <= other

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km >= other
