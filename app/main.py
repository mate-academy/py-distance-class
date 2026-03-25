from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_val(self, other: Union["Distance", Number]) -> Number:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        return Distance(self.km + self._get_val(other))

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        self.km += self._get_val(other)
        return self

    def __mul__(self, other: Number) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> "Distance":
        res = round(self.km / other, 2)
        return Distance(res)

    def __lt__(self, other: Union["Distance", Number]) -> bool:
        return self.km < self._get_val(other)

    def __gt__(self, other: Union["Distance", Number]) -> bool:
        return self.km > self._get_val(other)

    def __eq__(self, other: object) -> bool:
        return self.km == self._get_val(other)

    def __le__(self, other: Union["Distance", Number]) -> bool:
        return self.km <= self._get_val(other)

    def __ge__(self, other: Union["Distance", Number]) -> bool:
        return self.km >= self._get_val(other)
