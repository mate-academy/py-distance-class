class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> Distance:
        if isinstance(other, Distance):
            return Distance(other.km + self.km)
        else:
            return Distance(other + self.km)

    def __iadd__(self, other: float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km  # рядок 1: оновлюємо
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
