from typing import Union, Any


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def _get_km(self, other: Union["Distance", int, float])\
            -> Union[int, float]:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        self.km += self._get_km(other)
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km == self._get_km(other)
        return False

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        return self.km >= self._get_km(other)
