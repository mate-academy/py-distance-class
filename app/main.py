class Distance:
    def __init__(self, km: object) -> None:
        self.km = km

    def __str__(self) -> object:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> object:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> object:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: object) -> object:
        return Distance(self.km * other)

    def __truediv__(self, other: object) -> object:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: object) -> object:
        return self.km < other

    def __gt__(self, other: object) -> object:
        return self.km > other

    def __eq__(self, other: object) -> object:
        return self.km == other

    def __le__(self, other: object) -> object:
        return self.km <= other

    def __ge__(self, other: object) -> object:
        return self.km >= other
