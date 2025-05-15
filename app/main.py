class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> object:
        if other.__class__ is Distance:
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: object) -> object:
        if other.__class__ is Distance:
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: object) -> object:
        return Distance(self.km * other)

    def __truediv__(self, other: object) -> object:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: object) -> bool:
        if other.__class__ is Distance:
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: object) -> bool:
        if other.__class__ is Distance:
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: object) -> bool:
        if other.__class__ is Distance:
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: object) -> bool:
        if other.__class__ is Distance:
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: object) -> bool:
        if other.__class__ is Distance:
            return self.km >= other.km
        else:
            return self.km >= other
