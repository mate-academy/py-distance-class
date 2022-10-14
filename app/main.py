class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> object:
        if isinstance(other, (float, int)):
            return Distance(self.km + other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

    def __iadd__(self, value: int) -> object:
        if isinstance(value, (float, int)):
            self.km += value
            return self
        if isinstance(value, Distance):
            self.km += value.km
            return self

    def __mul__(self, other: int) -> object:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: float) -> object:
        if isinstance(other, (float, int)):
            return Distance(round((self.km / other), 2))

    def __lt__(self, other: float) -> bool:
        if isinstance(other, (float, int)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km

    def __gt__(self, other: float) -> bool:
        if isinstance(other, (float, int)):
            return self.km > other
        if isinstance(other, Distance):
            return self.km > other.km

    def __eq__(self, other: float) -> bool:
        if isinstance(other, (float, int)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km

    def __le__(self, other: float) -> bool:
        if isinstance(other, (float, int)):
            return self.km <= other
        if isinstance(other, Distance):
            return self.km <= other.km

    def __ge__(self, other: float) -> bool:
        if isinstance(other, (float, int)):
            return self.km >= other
        if isinstance(other, Distance):
            return self.km >= other.km

    def __len__(self) -> int:
        return len(self.km)
