from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, "Distance"]) -> object:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> object:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> object:
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km < other

    def __gt__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km > other

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km <= other

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km >= other
