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
        elif isinstance(distance2, (int, float)):
            return Distance(self.km + distance2)

    def __iadd__(self, distance2: Distance | float | int) -> Distance:
        if isinstance(distance2, Distance):
            self.km += distance2.km
        elif isinstance(distance2, (int, float)):
            self.km += distance2
        return self

    def __mul__(self, number: float | int) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: float | int) -> Distance:
        return Distance(round((self.km / number), 2))

    def __lt__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km < distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km < distance2

    def __gt__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km > distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km > distance2

    def __eq__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km == distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km == distance2

    def __le__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km <= distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km <= distance2

    def __ge__(self, distance2: Distance | float | int) -> bool:
        if isinstance(distance2, Distance):
            return self.km >= distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km >= distance2
