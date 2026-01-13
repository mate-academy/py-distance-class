from typing import Any, Union


def get_km(other: Any) -> float:
    """Help method to extract kilometers from Distance
    or return the number itself."""
    if isinstance(other, Distance):
        return other.km
    return other


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Any) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return None

    def __truediv__(self, other: Any) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return None

    def __lt__(self, other: Any) -> bool:
        return self.km < get_km(other)

    def __le__(self, other: Any) -> bool:
        return self.km <= get_km(other)

    def __eq__(self, other: Any) -> bool:
        return self.km == get_km(other)

    def __ne__(self, other: Any) -> bool:
        return self.km != get_km(other)

    def __gt__(self, other: Any) -> bool:
        return self.km > get_km(other)

    def __ge__(self, other: Any) -> bool:
        return self.km >= get_km(other)
