from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self,
                other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self,
                 other: Union[float, int, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self,
                factor: Union[float, int, "Distance"]) -> "Distance":
        return Distance(self.km * factor)

    def __truediv__(self,
                    divisor: Union[float, int, "Distance"]) -> "Distance":
        result = self.km / divisor
        return Distance(round(result, 2))

    def __lt__(self,
               other: Union[float, int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self,
               other: Union[float, int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self,
               other: Union[float, int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union[float, int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self,
               other: Union[float, int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
