class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> object:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: int) -> object:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self

    def __mul__(self, other: int) -> object:
        if isinstance(other, Distance):
            return Distance(self.km * other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, value: object) -> object:
        if isinstance(value, Distance):
            return Distance(round(self.km / value.km, 2))
        if isinstance(value, (int, float)):
            return Distance(round(self.km / value, 2))

    def __lt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
