class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (float, int)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (float, int)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("You can't divide by zero!")
            return Distance(round((self.km / other), 2))
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (float, int)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (float, int)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (float, int)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (float, int)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (float, int)):
            return self.km >= other
        return NotImplemented
