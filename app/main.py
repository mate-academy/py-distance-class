from __future__ import annotations


class Distance:

    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __iadd__(self, others: float | int | Distance) -> Distance:
        if isinstance(others, Distance):
            self.km += others.km
        else:
            self.km += others
        return self

    def __mul__(self, others: float | int) -> Distance:
        return Distance(self.km * others)

    def __truediv__(self, others: float | int) -> Distance:
        return Distance(round(self.km / others, 2))

    def __lt__(self, others: float | int | Distance) -> bool:
        if isinstance(others, Distance):
            return self.km < others.km
        else:
            return self.km < others

    def __gt__(self, others: float | int | Distance) -> bool:
        if isinstance(others, Distance):
            return self.km > others.km
        else:
            return self.km > others

    def __eq__(self, others: float | int | Distance) -> bool:
        if isinstance(others, Distance):
            return self.km == others.km
        else:
            return self.km == others

    def __le__(self, others: float | int | Distance) -> bool:
        if isinstance(others, Distance):
            return self.km <= others.km
        else:
            return self.km <= others

    def __ge__(self, others: float | int | Distance) -> bool:
        if isinstance(others, Distance):
            return self.km >= others.km
        else:
            return self.km >= others

    def __ne__(self, others: float | int | Distance) -> bool:
        if isinstance(others, Distance):
            return self.km != others.km
        else:
            return self.km != others

    def __sub__(self, others: float | int | Distance) -> None:
        if isinstance(others, Distance):
            self.km -= others.km
        else:
            self.km -= others
