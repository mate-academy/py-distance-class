from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            distance = self.km + other.km
        else:
            distance = self.km + other
        return Distance(distance)

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        distance2 = self.km * other
        return Distance(distance2)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        distance2 = round(self.km / other, 2)
        return Distance(distance2)

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        val_km = other.km if isinstance(other, Distance) else other
        return self.km < val_km

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        val_km = other.km if isinstance(other, Distance) else other
        return self.km > val_km

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        val_km = other.km if isinstance(other, Distance) else other
        return self.km == val_km

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        val_km = other.km if isinstance(other, Distance) else other
        return self.km <= val_km

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        val_km = other.km if isinstance(other, Distance) else other
        return self.km >= val_km
