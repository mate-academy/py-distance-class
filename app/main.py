from types import NotImplementedType


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km: int | float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _extract_km(other: object) -> int | float | NotImplementedType:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)) and not isinstance(other, bool):
            return other
        return NotImplemented

    def __add__(self, other: "Distance | int | float")\
            -> "Distance | NotImplementedType":
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other: "Distance | int | float")\
            -> "Distance | NotImplementedType":
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, factor: int | float) -> "Distance | NotImplementedType":
        if isinstance(factor, (int, float)) and not isinstance(factor, bool):
            return Distance(self.km * factor)
        return NotImplemented

    def __truediv__(self, divisor: int | float)\
            -> "Distance | NotImplementedType":
        if isinstance(divisor, (int, float)) and not isinstance(divisor, bool):
            return Distance(round(self.km / divisor, 2))
        return NotImplemented

    def __lt__(self, other: "Distance | int | float")\
            -> bool | NotImplementedType:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __gt__(self, other: "Distance | int | float") \
            -> bool | NotImplementedType:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other: object) -> bool:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return False
        return self.km == other_km

    def __le__(self, other: "Distance | int | float") \
            -> bool | NotImplementedType:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other: "Distance | int | float") \
            -> bool | NotImplementedType:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km
