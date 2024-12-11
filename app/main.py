from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        other = Distance.to_distance(other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        other = Distance.to_distance(other)
        self.km += other.km
        return self

    def __mul__(self, other: float | int) -> Distance:
        km = self.to_km(other)
        return Distance(self.km * km)

    @staticmethod
    def to_km(dist: int | float) -> float | int:
        if not (
                isinstance(dist, int)
                or isinstance(dist, float)
        ):
            raise TypeError
        return dist

    def __truediv__(self, other: Distance | float | int) -> Distance:
        km = Distance.to_km(other)
        return Distance(round(self.km / km, 2))

    def __eq__(self, other: Distance | float | int) -> bool:
        other = Distance.to_distance(other)
        return not (self.__lt__(other) or self.__gt__(other))

    def __lt__(self, other: Distance | float | int) -> bool:
        other = Distance.to_distance(other)
        return self.km < other.km

    def __le__(self, other: Distance | float | int) -> bool:
        other = Distance.to_distance(other)
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: Distance | float | int) -> bool:
        other = Distance.to_distance(other)
        return self.km > other.km

    def __ge__(self, other: Distance | float | int) -> bool:
        other = Distance.to_distance(other)

        return self.__gt__(other) or self.__eq__(other)

    @staticmethod
    def to_distance(other: Distance | int | float) -> Distance:
        if not (
                isinstance(other, Distance)
                or isinstance(other, int)
                or isinstance(other, float)
        ):
            raise TypeError
        if not isinstance(other, Distance):
            other = Distance(other)
        return other
