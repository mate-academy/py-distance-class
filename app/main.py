from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") ->\
            "Distance | NotImplemented":
        if isinstance(other, Distance):
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other: "Distance | int | float") ->\
            "Distance | NotImplemented":
        if isinstance(other, Distance):
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other: int | float) ->\
            "Distance | NotImplemented":
        if not isinstance(other, (int, float)):
            return NotImplemented
        new_km = self.km * other
        return Distance(new_km)

    def __truediv__(self, other: int | float) -> "Distance | NotImplemented":
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("division by zero")
        new_km = round(self.km / other, 2)
        return Distance(new_km)

    def _get_km(self, other: int | float) -> "Distance | NotImplemented":
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __eq__(self, other: "Distance | int | float")\
            -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km

    def __lt__(self, other: "Distance | int | float")\
            -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __le__(self, other: "Distance | int | float") -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other: "Distance | int | float") -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km

    def __gt__(self, other: "Distance | int | float") -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km
