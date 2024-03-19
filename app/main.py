from typing import Union
import math


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("wrong data type entered")
        if km < 0:
            raise ValueError("km cant be negative")
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, "Distance"]) -> "Distance":
        return Distance(
            self.km + (other.km if isinstance(other, Distance) else other)
        )

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        self.km += other.km if isinstance(other, Distance) else other
        return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Union[int, "Distance"]) -> bool:
        return math.isclose(
            self.km,
            (other.km if isinstance(other, Distance) else other)
        )

    def __gt__(self, other: Union[int, "Distance"]) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)
