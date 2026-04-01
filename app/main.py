from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _get_value(other: Union["Distance", Number]) -> Number:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return Distance(self.km + value)

    def __radd__(self, other: Union["Distance", Number]) -> "Distance":
        return self.__add__(other)

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other: Number) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: Number) -> "Distance":
        return self.__mul__(other)

    def __truediv__(self, other: Number) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Union["Distance", Number]) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km < value

    def __gt__(self, other: Union["Distance", Number]) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km > value

    def __eq__(self, other: Union["Distance", Number]) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km == value

    def __le__(self, other: Union["Distance", Number]) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other: Union["Distance", Number]) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km >= value
