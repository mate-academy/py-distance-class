from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, val2: Union["Distance", float, int]) -> "Distance":
        if isinstance(val2, Distance):
            return Distance(self.km + val2.km)
        else:
            return Distance(self.km + val2)

    def __iadd__(self, val2: Union["Distance", float, int]) -> "Distance":
        if isinstance(val2, Distance):
            self.km += val2.km
        else:
            self.km += val2
        return self

    def __mul__(self, val2: Union[float, int]) -> "Distance":
        return Distance(self.km * val2)

    def __truediv__(self, val2: Union[float, int]) -> "Distance":
        return Distance(round(self.km / val2, 2))

    def __lt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
