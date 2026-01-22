class Distance:
    # Write your code here
    def __init__(self, km: int) -> int:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> int:
        other_km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + other_km)

    def __mul__(self, other: int) -> int:
        new_num = self.km * other
        return Distance(new_num)

    def __iadd__(self, other: int) -> int:
        other_km = other.km if isinstance(other, Distance) else other
        self.km += other_km
        return self

    def __truediv__(self, other: int) -> int:
        new_num = round(self.km / other, 2)
        return Distance(new_num)

    def __lt__(self, other: int) -> bool:
        return self.km < other

    def __gt__(self, other: int) -> bool:
        return self.km > other

    def __eq__(self, other: int) -> bool:
        return self.km == other

    def __le__(self, other: int) -> bool:
        return self.km <= other

    def __ge__(self, other: int) -> bool:
        return self.km >= other
