from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Can only add Distance objects or numbers")

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Can only add Distance objects or numbers")
        return self

    def __mul__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Can only multiply Distance "
                            "by an integer or float")

    def __truediv__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            result = self.km / other
            return Distance(round(result, 2))
        else:
            raise TypeError("Can only div Distance by an integer or float")

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Can only compare Distance objects or numbers")

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Can only compare Distance objects or numbers")

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Can only compare Distance objects or numbers")

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Can only compare Distance objects or numbers")

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Can only compare Distance objects or numbers")
