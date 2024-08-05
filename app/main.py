class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            km = self.km + other
        else:
            km = self.km + other.km
        return Distance(km=km)

    def __iadd__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: int) -> int:
        km = self.km * other
        return Distance(km=km)

    def __truediv__(self, other: int) -> float:
        km = round(self.km / other, 2)
        return Distance(km=km)

    def __lt__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        return self.km >= other.km
