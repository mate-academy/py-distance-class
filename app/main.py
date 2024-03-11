from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, addentum: object | int) -> Distance:
        return Distance(self.km + getattr(addentum, "km", addentum))

    def __iadd__(self, addentum: object | int) -> Distance:
        self.km += getattr(addentum, "km", addentum)
        return self

    def __mul__(self, multiplier: int) -> Distance:
        self.km *= multiplier
        return self

    def __truediv__(self, divider: int) -> Distance:
        if divider == 0:
            return float("inf")
        self.km = round(self.km / divider, 2)
        return self

    def __lt__(self, comparer: object | int) -> bool:
        return self.km < getattr(comparer, "km", comparer)

    def __gt__(self, comparer: object | int) -> bool:
        return self.km > getattr(comparer, "km", comparer)

    def __eq__(self, comparer: object | int) -> bool:
        return self.km == getattr(comparer, "km", comparer)

    def __le__(self, comparer: object | int) -> bool:
        return not self.km > getattr(comparer, "km", comparer)

    def __ge__(self, comparer: object | int) -> bool:
        return not self.km < getattr(comparer, "km", comparer)
