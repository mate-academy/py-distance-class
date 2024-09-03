from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: Distance | int | float) -> Distance:
        if isinstance(distance, Distance):
            total = self.km + distance.km
        else:
            total = self.km + distance

        return Distance(total)

    def __iadd__(self, distance: Distance | int | float) -> Distance:
        if isinstance(distance, Distance):
            self.km += distance.km
        else:
            self.km += distance

        return self

    def __mul__(self, km: int | float) -> Distance:
        return Distance(self.km * km)

    def __truediv__(self, km: int | float) -> Distance:
        total = round(self.km / km, 2)

        return Distance(total)
