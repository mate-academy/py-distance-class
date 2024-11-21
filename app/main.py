from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other_km: Distance | int) -> Distance:
        if isinstance(other_km, Distance):
            return Distance(self.km + other_km.km)
        return Distance(self.km + other_km)

    def __iadd__(self, other_km: Distance | int) -> Distance:
        if isinstance(other_km, Distance):
            self.km += other_km.km
        else:
            self.km += other_km
        return self

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __mul__(self, multiplier: int) -> Distance:
        return Distance(self.km * multiplier)

    def __truediv__(self, divider: int) -> Distance:
        return Distance(round(self.km / divider, 2))

    def __lt__(self, kilometers: Distance | (int, float)) -> bool:
        if isinstance(kilometers, Distance):
            return self.km < kilometers.km
        return self.km < kilometers

    def __gt__(self, kilometers: Distance | int) -> bool:
        if isinstance(kilometers, Distance):
            return self.km > kilometers.km
        return self.km > kilometers

    def __eq__(self, kilometers: Distance | int) -> bool:
        if isinstance(kilometers, Distance):
            return self.km == kilometers.km
        return self.km == kilometers

    def __le__(self, kilometers: Distance | int) -> bool:
        if isinstance(kilometers, Distance):
            return self.km <= kilometers.km
        return self.km <= kilometers

    def __ge__(self, kilometers: Distance | int) -> bool:
        if isinstance(kilometers, Distance):
            return self.km >= kilometers.km
        return self.km >= kilometers
