from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> Distance:
        if type(other) == Distance:
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other) -> Distance:
        if type(other) == Distance:
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other) -> bool:
        if type(other) == Distance:
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other) -> bool:
        return not self.km <= other

    def __eq__(self, other) -> bool:
        if type(other) == Distance:
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other) -> bool:
        if type(other) == Distance:
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other) -> bool:
        return not self.km < other

    def __len__(self) -> int:
        return self.km
