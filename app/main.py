class Distance:
    def __init__(self, km) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometres."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> "Distance":
        if isinstance(other, int):
            other = Distance(other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other) -> "Distance":
        if isinstance(other, int):
            other = Distance(other)
        self.km += other.km
        return self

    def __mul__(self, other) -> "Distance":
        if isinstance(other, int):
            other = Distance(other)
        return Distance(km=self.km * other.km)

    def __truediv__(self, other) -> "Distance":
        if isinstance(other, int):
            other = Distance(other)
        return Distance(km=round(self.km / other.km, 2))

    def __lt__(self, other) -> bool:
        if isinstance(other, int):
            other = Distance(other)
        return self.km < other.km

    def __gt__(self, other) -> bool:
        if isinstance(other, int):
            other = Distance(other)
        return self.km > other.km

    def __le__(self, other) -> bool:
        if isinstance(other, int):
            other = Distance(other)
        return self.km <= other.km

    def __ge__(self, other) -> bool:
        if isinstance(other, int):
            other = Distance(other)
        return self.km >= other.km

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            other = Distance(other)
        return self.km == other.km

    def __len__(self) -> int:
        return self.km
