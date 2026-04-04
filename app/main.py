from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance2: Distance | float | int) -> Distance:
        if isinstance(distance2, Distance):
            return Distance(self.km + distance2.km)
        return Distance(self.km + distance2)

    def __iadd__(self, distance2: Distance | float | int) -> Distance:
        if isinstance(distance2, Distance):
            self.km += distance2.km
        else:
            self.km += distance2
        return self

    def __mul__(self, factor: float | int) -> Distance:
        product = self.km * factor
        return Distance(product)

    def __truediv__(self, divider: float | int) -> Distance:
        division = round(self.km / divider, 2)
        return Distance(division)

    def __lt__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km < distance2.km
        return self.km < distance2

    def __gt__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km > distance2.km
        return self.km > distance2

    def __eq__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km == distance2.km
        return self.km == distance2

    def __le__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km <= distance2.km
        return self.km <= distance2

    def __ge__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km >= distance2.km
        return self.km >= distance2
