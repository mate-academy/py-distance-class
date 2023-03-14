from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", float]) -> "Distance":
        km = self.km + other.km if isinstance(other, Distance) \
            else self.km + other
        return Distance(km)

    def __iadd__(self, other: Union["Distance", float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: float) -> "Distance":
        km = self.km * other
        return Distance(km)

    def __truediv__(self, other: float) -> "Distance":
        km = round(self.km / other, 2)
        return Distance(km)

    def __lt__(self, other: Union["Distance", float]) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km < km

    def __gt__(self, other: Union["Distance", float]) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km > km

    def __eq__(self, other: Union["Distance", float]) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km == km

    def __le__(self, other: Union["Distance", float]) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km <= km

    def __ge__(self, other: Union["Distance", float]) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km >= km
