from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def other_km(self, other: Union["Distance", Number]) -> Number:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        return Distance(self.km + self.other_km(other))

    def __radd__(self, other: Union["Distance", Number]) -> "Distance":
        return Distance(self.other_km(other) + self.km)

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        self.km += self.other_km(other)
        return self

    def __mul__(self, other: Number) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Cannot multiply Distance by Distance")
        return Distance(self.km * other)

    def __rmul__(self, other: Number) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Cannot multiply Distance by Distance")
        return Distance(other * self.km)

    def __truediv__(self, other: Number) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Cannot divide Distance by Distance")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union["Distance", Number]) -> bool:
        return self.km < self.other_km(other)

    def __gt__(self, other: Union["Distance", Number]) -> bool:
        return self.km > self.other_km(other)

    def __eq__(self, other: Union["Distance", Number]) -> bool:
        return self.km == self.other_km(other)

    def __le__(self, other: Union["Distance", Number]) -> bool:
        return self.km <= self.other_km(other)

    def __ge__(self, other: Union["Distance", Number]) -> bool:
        return self.km >= self.other_km(other)
