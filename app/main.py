from __future__ import annotations, division


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {round(self.km, 2)} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={round(self.km, 2)})"

    def __add__(self, distance: Distance | int | float) -> Distance:
        if isinstance(distance, (int, float)):
            return Distance(self.km + distance)
        return Distance(self.km + distance.km)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, distance: int) -> Distance:
        return Distance(self.km * distance)

    def __truediv__(self, distance: int) -> Distance:
        return Distance(round(self.km / distance, 2))

    def __lt__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km < distance.km
        return self.km < distance

    def __gt__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km > distance.km
        return self.km > distance

    def __eq__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km == distance.km
        return self.km == distance

    def __le__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km <= distance.km
        return self.km <= distance

    def __ge__(self, distance: Distance | int | float) -> bool:
        if isinstance(distance, Distance):
            return self.km >= distance.km
        return self.km >= distance
