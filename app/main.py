from typing import Union

Number = Union[int, float]


class Distance:
    km: Number

    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # --- helpers ---
    def _get_km(self, other: Union["Distance", Number]) -> Union[Number, type(NotImplemented)]:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    # --- arithmetic ---
    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return Distance(self.km + km)

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        self.km += km
        return self

    def __mul__(self, other: Number) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(round(self.km / other, 2))

    # --- comparisons ---
    def __lt__(self, other: Union["Distance", Number]) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km < km

    def __le__(self, other: Union["Distance", Number]) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km <= km

    def __gt__(self, other: Union["Distance", Number]) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km > km

    def __ge__(self, other: Union["Distance", Number]) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km >= km

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return False
        km = self._get_km(other)
        return self.km == km