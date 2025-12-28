from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, distance: int | float) -> Distance:
        if isinstance(distance, (int, float)):
            return Distance(self.km * distance)
        return NotImplemented

    def __truediv__(self, distance: int | float) -> Distance:
        if isinstance(distance, (int, float)):
            return Distance(round(self.km / distance, 2))
        return NotImplemented

    def __lt__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km < distance.km
        elif isinstance(distance, (int, float)):
            return self.km < distance
        return NotImplemented

    def __gt__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km > distance.km
        elif isinstance(distance, (int, float)):
            return self.km > distance
        return NotImplemented

    def __eq__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km == distance.km
        elif isinstance(distance, (int, float)):
            return self.km == distance
        return NotImplemented

    def __le__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km <= distance.km
        elif isinstance(distance, (int, float)):
            return self.km <= distance
        return NotImplemented

    def __ge__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km >= distance.km
        elif isinstance(distance, (int, float)):
            return self.km >= distance
        return NotImplemented
