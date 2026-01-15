from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def get_km_from_type(distance: Distance | int | float) -> int | float:
        if isinstance(distance, Distance):
            return distance.km
        elif isinstance(distance, (int, float)):
            return distance
        else:
            raise TypeError

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.get_km_from_type(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.get_km_from_type(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.get_km_from_type(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.get_km_from_type(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.get_km_from_type(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self.get_km_from_type(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self.get_km_from_type(other)
