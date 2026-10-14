class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> Distance:
        if isinstance(other, Distance):
            total = self.km + other.km
        else:
            total = self.km + other

        return Distance(total)

    def __iadd__(self, other: object) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other

        return self

    def __mul__(self, other: object) -> Distance:
        total = self.km * other
        return Distance(total)

    def __truediv__(self, other: object) -> Distance:
        total = round(self.km / other, 2)
        return Distance(total)

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            total = self.km < other.km
        else:
            total = self.km < other

        return total

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            total = self.km > other.km
        else:
            total = self.km > other

        return total

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            total = self.km == other.km
        else:
            total = self.km == other

        return total

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            total = self.km <= other.km
        else:
            total = self.km <= other

        return total

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            total = self.km >= other.km
        else:
            total = self.km >= other

        return total
