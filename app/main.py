from __future__ import annotations


class Distance:
    def __init__(self, km: int or float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int or float) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, other: int or float) -> Distance:
        if isinstance(other, (int, float)):
            self.km *= other
            return self
        else:
            raise TypeError(f"{other} is not int")

    def __truediv__(self, other: int or float) -> Distance:
        if isinstance(other, (int, float)):
            self.km /= other
            self.km = round(self.km, 2)
            return self
        else:
            raise TypeError(f"{other} is not int")

    def __lt__(self, other: Distance or int or float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other: Distance or int or float) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other: Distance or int or float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other: Distance or int or float) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other: Distance or int or float) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        else:
            return self.km >= other.km
