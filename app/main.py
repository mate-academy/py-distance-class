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
            distance = self.km + other.km
        else:
            distance = self.km + other
        return Distance(distance)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        distance = self.km * other
        return Distance(distance)

    def __truediv__(self, other: int | float) -> Distance:
        distance = round(self.km / other, 2)
        return Distance(distance)

    def __lt__(self, other: Distance | int | float) -> bool:
        get_km = other.km if isinstance(other, Distance) else other
        return self.km < get_km

    def __gt__(self, other: Distance | int | float) -> bool:
        get_km = other.km if isinstance(other, Distance) else other
        return self.km > get_km

    def __eq__(self, other: Distance | int | float) -> bool:
        get_km = other.km if isinstance(other, Distance) else other
        return self.km == get_km

    def __le__(self, other: Distance | int | float) -> bool:
        get_km = other.km if isinstance(other, Distance) else other
        return self.km <= get_km

    def __ge__(self, other: Distance | int | float) -> bool:
        get_km = other.km if isinstance(other, Distance) else other
        return self.km >= get_km
