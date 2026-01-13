from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # --- Addition ---
    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    # --- Multiplication ---
    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    # --- True division ---
    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    # --- Helper for comparisons ---
    def _get_km(self, other: Union["Distance", int, float]) -> float:
        if isinstance(other, Distance):
            return other.km
        return other

    # --- Comparison operators ---
    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km < self._get_km(other)

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        return self.km <= self._get_km(other)

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        return self.km == self._get_km(other)

    def __ne__(self, other: Union["Distance", int, float]) -> bool:
        return self.km != self._get_km(other)

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km > self._get_km(other)

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        return self.km >= self._get_km(other)
