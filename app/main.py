from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> object:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        return Distance(km=self.km + other)

    def __iadd__(self, other: Union["Distance", int, float]) -> object:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other
        return self

    def __mul__(self, other: Union[int, float]) -> object:
        return Distance(km=self.km * other)

    def __truediv__(self, other: Union[int, float]) -> object:
        if other != 0:
            res_km = round((self.km / other), 2)
            return Distance(km=res_km)

    def __lt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, (int, float)):
            return not self.km > other
        return not self.km > other.km

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return not self.km < other
        return not self.km < other.km
