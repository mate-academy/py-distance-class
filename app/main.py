class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: callable) -> object:
        if isinstance(other, int | float) is True:
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: callable) -> object:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int | float) -> int | object:
        if isinstance(other, int | float):
            return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> object:
        if isinstance(other, int | float):
            return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    def __gt__(self, other: int | float) -> bool:
        return self.km > other

    def __eq__(self, other: int | float) -> bool:
        return self.km == other

    def __le__(self, other: int | float) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        return self.km >= other

    def __len__(self) -> object:
        len_distance = range(1, self.km + 1)

        return len_distance
