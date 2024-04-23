from typing import Callable
from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def operate(self, other: Union[int, "Distance"], operation: Callable) -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=operation(self.km, other.km))
        else:
            return Distance(km=operation(self.km, other))

    def compare(self, other: Union[int, "Distance"], comparison) -> bool:
        if isinstance(other, Distance):
            return comparison(self.km, other.km)
        else:
            return comparison(self.km, other)

    def __add__(self, other: Union[int, "Distance"]) -> "Distance":
        return self.operate(other, lambda x, y: x + y)

    def __iadd__(self, other: Union[int, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(km=self.km * other)

    def __truediv__(self, other: int) -> "Distance":
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Union[int, "Distance"]) -> bool:
        return self.compare(other, lambda x, y: x < y)

    def __gt__(self, other: Union[int, "Distance"]) -> bool:
        return self.compare(other, lambda x, y: x > y)

    def __eq__(self, other: Union[int, "Distance"]) -> bool:
        return self.compare(other, lambda x, y: x == y)

    def __le__(self, other: Union[int, "Distance"]) -> bool:
        return self.compare(other, lambda x, y: x <= y)

    def __ge__(self, other: Union[int, "Distance"]) -> bool:
        return self.compare(other, lambda x, y: x >= y)

