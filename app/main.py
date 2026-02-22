from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, dist: int | float | Distance) -> Distance:
        if isinstance(dist, Distance):
            return Distance(self.km + dist.km)
        return Distance(self.km + dist)

    def __iadd__(self, dist: int | float | Distance) -> Distance:
        if isinstance(dist, Distance):
            self.km += dist.km
            return self
        self.km += dist
        return self

    def __mul__(self, mul: int | float) -> Distance:
        return Distance(self.km * mul)

    def __truediv__(self, div: int | float) -> Distance:
        return Distance(round((self.km / div), 2))

    def __lt__(self, dist: int | float | Distance) -> bool:
        if isinstance(dist, Distance):
            return self.km < dist.km
        return self.km < dist

    def __gt__(self, dist: int | float | Distance) -> bool:
        if isinstance(dist, Distance):
            return self.km > dist.km
        return self.km > dist

    def __eq__(self, dist: int | float | Distance) -> bool:
        if isinstance(dist, Distance):
            return self.km == dist.km
        return self.km == dist

    def __le__(self, dist: int | float | Distance) -> bool:
        if isinstance(dist, Distance):
            return self.km <= dist.km
        return self.km <= dist

    def __ge__(self, dist: int | float | Distance) -> bool:
        if isinstance(dist, Distance):
            return self.km >= dist.km
        return self.km >= dist
