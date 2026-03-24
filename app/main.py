from typing import Union


class Distance:

    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __mul__(self, number: Union[int, float]) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: Union[int, float]) -> "Distance":
        return Distance(round(self.km / number, 2))

    def _get_value(self, other: Union["Distance", int, float])\
            -> Union[int, float]:
        return other.km if isinstance(other, Distance) else other

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km < self._get_value(other)

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km > self._get_value(other)

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        return self.km == self._get_value(other)

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        return self.km <= self._get_value(other)

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        return self.km >= self._get_value(other)
