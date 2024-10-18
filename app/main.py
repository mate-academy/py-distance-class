class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: callable) -> callable:
        if not isinstance(other, (int, float)):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: callable) -> callable:
        if not isinstance(other, (int, float)):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: int) -> callable:
        return Distance(self.km * other)

    def __truediv__(self, other: callable) -> callable:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int) -> callable:
        return self.km < other

    def __gt__(self, other: int) -> callable:
        return self.km > other

    def __eq__(self, other: int) -> callable:
        return self.km == other

    def __le__(self, other: int) -> callable:
        return self.km <= other

    def __ge__(self, other: int) -> callable:
        return self.km >= other
