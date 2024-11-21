class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> int:
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        if isinstance(other, (int, float)):
            self.km = self.km + other
            return self

    def __iadd__(self, other: int) -> int:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: int) -> int:
        if isinstance(other, (int, float)):
            self.km = self.km * other
            return self
        else:
            return self.km * other

    def __truediv__(self, other: int) -> float:
        if isinstance(other, (int, float)):
            self.km = round(self.km / other, 2)
            return self
        else:
            return round(self.km / other, 2)

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

    def __len__(self: int) -> int:
        return self.km
