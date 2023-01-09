class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> object:
        if isinstance(other, Distance):
            result = Distance(self.km + other.km)
        else:
            result = Distance(self.km + other)
        return result

    def __iadd__(self, other: object) -> object:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: object) -> object:
        self.km *= other
        return self

    def __truediv__(self, other: object) -> object:
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: object) -> object:
        if isinstance(other, Distance):
            result = self.km < other.km
        else:
            result = self.km < other
        return result

    def __gt__(self, other: object) -> object:
        if isinstance(other, Distance):
            result = self.km > other.km
        else:
            result = self.km > other
        return result

    def __eq__(self, other: object) -> object:
        if isinstance(other, Distance):
            result = self.km == other.km
        else:
            result = self.km == other
        return result

    def __le__(self, other: object) -> object:
        if isinstance(other, Distance):
            result = self.km <= other.km
        else:
            result = self.km <= other
        return result

    def __ge__(self, other: object) -> object:
        if isinstance(other, Distance):
            result = self.km >= other.km
        else:
            result = self.km >= other
        return result
