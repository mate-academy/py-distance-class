from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return (f"Distance: {self.km} kilometers.")

    def __repr__(self) -> str:
        return (f"Distance(km={self.km})")  # "Distance(km=20)"

    def __add__(self, another_km: Distance) -> Distance:
        if isinstance(another_km, Distance):
            return Distance(self.km + another_km.km)
        return Distance(self.km + another_km)

    def __iadd__(self, another_km: Distance) -> Distance:
        if isinstance(another_km, Distance):
            self.km += another_km.km
        else:
            self.km += another_km
        return self

    def __mul__(self, mul: int) -> Distance:
        return Distance(self.km * mul)

    def __truediv__(self, div: int) -> Distance:
        return Distance(round(self.km / div, 2))

    def __lt__(self, another_km: Distance) -> bool:
        return self.km < another_km

    def __gt__(self, another_km: Distance) -> bool:
        return self.km > another_km

    def __eq__(self, another_km: Distance) -> bool:
        return self.km == another_km

    def __le__(self, another_km: Distance) -> bool:
        return self.km <= another_km

    def __ge__(self, another_km: Distance) -> bool:
        return self.km >= another_km
