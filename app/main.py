from numbers import Number


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> object:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, Number):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: Number) -> object:
        if isinstance(other, Number):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, Number):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: Number) -> object:
        if isinstance(other, Number):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: Number) -> object:
        if isinstance(other, Number):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Number) -> object:
        if isinstance(other, Number):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, Number):
            return self.km == other
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, Number):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, Number):
            return self.km > other
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, Number):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, Number):
            return self.km >= other
        return NotImplemented
