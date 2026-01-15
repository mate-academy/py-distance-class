from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, self.__class__):
            new_km = self.km + other.km
        elif isinstance(other, (int, float)):
            new_km = self.km + other
        else:
            return NotImplemented
        return self.__class__(new_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, self.__class__):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            new_km = self.km * other
            return self.__class__(new_km)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            new_km = round(self.km / other, 2)
            return self.__class__(new_km)
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, self.__class__):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, self.__class__):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, self.__class__):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, self.__class__):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, self.__class__):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
