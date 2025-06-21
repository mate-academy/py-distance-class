class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError
        return self

    def __mul__(self, other: object) -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError
        return Distance(self.km * other)

    def __truediv__(self, other: object) -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
