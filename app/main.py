from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if not isinstance(other, Distance):
            return Distance(self.km + other)

        return Distance(self.km + other.km)

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if not isinstance(other, Distance):
            self.km += other
            return self

        self.km += other.km
        return self

    def __mul__(self, multiplier: int | float) -> "Distance":
        return Distance(self.km * multiplier)

    def __truediv__(self, divisor: int | float) -> "Distance":
        return Distance(round(self.km / divisor, 2))

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, Distance):
            return self.km == other

        return self.km == other.km

    def __ne__(self, other: "Distance") -> bool:
        return not self.__eq__(other)

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, Distance):
            return self.km > other

        return self.km > other.km

    def __ge__(self, other: "Distance") -> bool:
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other: "Distance") -> bool:
        return not self.__ge__(other)

    def __le__(self, other: "Distance") -> bool:
        return self.__lt__(other) or self.__eq__(other)
