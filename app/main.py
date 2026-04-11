from typing import Any


class Distance:
    def __init__(self,km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            second_distance = other.km
        else:
            second_distance = other
        return Distance(km=self.km + second_distance)

    def __iadd__(self, other: Any) -> Distance:

        if isinstance(other, Distance):
            other_distance  = other.km
        else:
            other_distance  = other
        self.km += other_distance
        return self

