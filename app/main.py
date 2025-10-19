from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __mul__(self, other: Union[int, float]) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if not isinstance(other, (int, float)) or other == 0:
            return NotImplemented

        rounded_km = round(self.km / other, 2)
        return Distance(rounded_km)

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def _get_other_km(self, other: Union["Distance", int, float])\
            -> float | None:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return None

    def __lt__(self, other: Union["Distance", int, float])\
            -> Union[bool, type(NotImplemented)]:
        other_km = self._get_other_km(other)
        if other_km is None:
            return NotImplemented
        return self.km < other_km

    def __gt__(self, other: Union["Distance", int, float])\
            -> Union[bool, type(NotImplemented)]:
        other_km = self._get_other_km(other)
        if other_km is None:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other: Union["Distance", int, float])\
            -> bool:
        other_km = self._get_other_km(other)
        if other_km is None:
            return False
        return self.km == other_km

    def __le__(self, other: Union["Distance", int, float])\
            -> Union[bool, type(NotImplemented)]:
        other_km = self._get_other_km(other)
        if other_km is None:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other: Union["Distance", int, float])\
            -> Union[bool, type(NotImplemented)]:
        other_km = self._get_other_km(other)
        if other_km is None:
            return NotImplemented
        return self.km >= other_km
