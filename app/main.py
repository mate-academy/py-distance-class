from __future__ import annotations


class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> Distance:
        return Distance(
            self.km + other.real
            if isinstance(other, (int, float))
            else self.km + other.km
        )

    def __iadd__(self, other) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other.real
        else:
            self.km += other.km
        return self

    def __mul__(self, other) -> Distance:
        return Distance(
            self.km * other.real if isinstance(other, (int, float))
            else self.km * other.km
        )

    def __truediv__(self, other) -> Distance:
        return Distance(
            round(self.km / other.real, 2) if isinstance(other, (int, float))
            else round(self.km / other.km, 2)
        )

    def __lt__(self, other) -> bool:
        return self.km < other.real if isinstance(other, (int, float)) \
            else self.km < other.km

    def __gt__(self, other) -> bool:
        return self.km > other.real if isinstance(other, (int, float)) \
            else self.km > other.km

    def __eq__(self, other) -> bool:
        return self.km == other.real if isinstance(other, (int, float)) \
            else self.km == other.km

    def __le__(self, other) -> bool:
        return not self > other

    def __ge__(self, other) -> bool:
        return not self < other

    def __len__(self) -> float:
        return self.km
