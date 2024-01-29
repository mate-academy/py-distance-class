from typing import Callable


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _operate(self, other: "Distance", operation: Callable) -> "Distance":
        if isinstance(other, Distance):
            return Distance(operation(self.km, other.km))
        elif isinstance(other, (int, float)):
            return Distance(operation(self.km, other))

    def __add__(self, other: "Distance") -> "Distance":
        return self._operate(other, lambda x, y: x + y)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other

        return self

    def __mul__(self, factor: float) -> "Distance":
        return self._operate(Distance(factor), lambda x, y: x * y)

    def __truediv__(self, divisor: float) -> "Distance":
        return self._operate(Distance(divisor), lambda x, y: round(x / y, 2))

    def _compare(self, other: "Distance", operation: Callable) -> bool:
        if isinstance(other, Distance):
            return operation(self.km, other.km)
        elif isinstance(other, (int, float)):
            return operation(self.km, other)

    def __lt__(self, other: "Distance") -> bool:
        return self._compare(other, lambda x, y: x < y)

    def __gt__(self, other: "Distance") -> bool:
        return self._compare(other, lambda x, y: x > y)

    def __eq__(self, other: "Distance") -> bool:
        return self._compare(other, lambda x, y: x == y)

    def __le__(self, other: "Distance") -> bool:
        return self._compare(other, lambda x, y: x <= y)

    def __ge__(self, other: "Distance") -> bool:
        return self._compare(other, lambda x, y: x >= y)
