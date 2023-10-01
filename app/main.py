from __future__ import annotations


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_km: Distance | float) -> Distance:
        if isinstance(other_km, Distance):
            return Distance(self.km + other_km.km)
        elif isinstance(other_km, (float, int)):
            return Distance(self.km + other_km)
        else:
            raise ValueError("Unsupported type for addition")

    def __iadd__(self, other_km: Distance | float) -> Distance:
        if isinstance(other_km, Distance):
            self.km += other_km.km
        elif isinstance(other_km, (float, int)):
            self.km += other_km
        else:
            raise ValueError("Unsupported type for iaddition")
        return self

    def __mul__(self, other_km: float) -> Distance:
        if not isinstance(other_km, (float, int)):
            raise TypeError("Unsupported type for multiplication")

        return Distance(self.km * other_km)

    def __truediv__(self, other_km: float) -> Distance:
        if not isinstance(other_km, (int, float)):
            raise TypeError("Unsupported type for division")
        return Distance(round(self.km / other_km, 2))

    def __lt__(self, other_km: Distance | float | int) -> bool:
        if isinstance(other_km, Distance):
            return self.km < other_km.km
        elif isinstance(other_km, (float, int)):
            return self.km < other_km
        else:
            raise ValueError("Can't compare Distance with non-Distance type")

    def __gt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (float, int)):
            return self.km > other
        else:
            raise ValueError("Can't compare Distance with non-Distance type")

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (float, int)):
            return self.km == other
        else:
            raise ValueError("Can't compare Distance with non-Distance type")

    def __le__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (float, int)):
            return self.km <= other
        else:
            raise ValueError("Can't compare Distance with non-Distance type")

    def __ge__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (float, int)):
            return self.km >= other
        else:
            raise ValueError("Can't compare Distance with non-Distance type")
