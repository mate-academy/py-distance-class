from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + float(other))

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += float(other)
        return self

    def __mul__(self, other: Number) -> "Distance":
        return Distance(self.km * float(other))

    def __truediv__(self, other: Number) -> "Distance":
        result: float = round(self.km / float(other), 2)
        return Distance(result)

    def _get_value(self, other: Union["Distance", Number]) -> float:
        return other.km if isinstance(other, Distance) else float(other)

    def __lt__(self, other: Union["Distance", Number]) -> bool:
        return self.km < self._get_value(other)

    def __gt__(self, other: Union["Distance", Number]) -> bool:
        return self.km > self._get_value(other)

    def __eq__(self, other: Union["Distance", Number]) -> bool:
        return self.km == self._get_value(other)

    def __le__(self, other: Union["Distance", Number]) -> bool:
        return self.km <= self._get_value(other)

    def __ge__(self, other: Union["Distance", Number]) -> bool:
        return self.km >= self._get_value(other)
