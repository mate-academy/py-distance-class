class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> None:
        print(f"Distance: {self.km} kilometers.")

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> int:
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance) -> None:
        self.km += other.km

    def __mul__(self, other: Distance) -> float:
        return Distance(self.km * other.km)

    def __truediv__(self, other: Distance) -> float:
        if isinstance(other, Distance):
            return Distance(self.km / other.km)

    def __lt__(self, other: Distance) -> bool:
        return self.km < other.km

    def __gt__(self, other: Distance) -> bool:
        return self.km > other.km

    def __eq__(self, other: Distance) -> bool:
        return self.km == other.km

    def __le__(self, other: Distance) -> bool:
        return self.km <= other.km

    def __ge__(self, other: Distance) -> bool:
        return self.km >= other.km
