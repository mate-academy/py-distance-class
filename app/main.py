class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __eq__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __lt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __le__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __gt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __ge__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented

    def __add__(self, other: float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(other + self.km)
        return NotImplemented

    def __iadd__(self, other: float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: float) -> "Distance":
        return self.__mul__(other)

    def __truediv__(self, other: float) -> "Distance":
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = round(self.km / other, 2)
        return Distance(result)
