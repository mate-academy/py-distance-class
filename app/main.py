from typing import Union


class Distance:
    def __init__(self, km: Union[float, int]) -> None:
        self.km = float(km)

    def __str__(self) -> str:
        km_str = str(int(self.km)) if self.km.is_integer() else str(self.km)
        return f"Distance: {km_str} kilometers."  # Убрал \n в конце

    def __repr__(self) -> str:
        km_str = str(int(self.km)) if self.km.is_integer() else str(self.km)
        return f"Distance(km={km_str})"

    def __add__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Union[float, int]) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Union[float, int]) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other
