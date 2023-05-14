from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        kilometers = other.km if isinstance(other, Distance) else other
        return Distance(km=self.km + kilometers)

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        kilometers = other.km if isinstance(other, Distance) else other
        self.km += kilometers
        return self

    def __mul__(self, other: Union[int, float, "Distance"]) -> "Distance":
        self.km *= other
        return self

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        km = self.km / other
        return Distance(km=round(km, 2))

    def __lt__(self, other: Union[int, float, "Distance"]) -> "Distance":
        kilometers = other.km if isinstance(other, Distance) else other
        return self.km < kilometers

    def __gt__(self, other: Union[int, float, "Distance"]) -> "Distance":
        kilometers = other.km if isinstance(other, Distance) else other
        return self.km > kilometers

    def __eq__(self, other: Union[int, float, "Distance"]) -> "Distance":
        kilometers = other.km if isinstance(other, Distance) else other
        return self.km == kilometers

    def __le__(self, other: Union[int, float, "Distance"]) -> "Distance":
        kilometers = other.km if isinstance(other, Distance) else other
        return self.km <= kilometers

    def __ge__(self, other: Union[int, float, "Distance"]) -> "Distance":
        kilometers = other.km if isinstance(other, Distance) else other
        return self.km >= kilometers
