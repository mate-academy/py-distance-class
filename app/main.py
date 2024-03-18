import operator
from typing import Union, Callable


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported type for addition.")

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported type for in-place addition.")
        return self

    def __mul__(self, other: float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported type for multiplication.")

    def __truediv__(self, other: Union[float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        elif isinstance(other, Distance):
            raise TypeError("Unsupported operation.")
        else:
            raise TypeError("Unsupported type for division.")

    def _compare_with_operand(
            self,
            other: Union["Distance", float],
            comparison_operator: Callable
    ) -> bool:
        if isinstance(other, Distance):
            return comparison_operator(self.km, other.km)
        elif isinstance(other, (int, float)):
            return comparison_operator(self.km, other)
        else:
            raise TypeError("Unsupported type for comparison.")

    def __lt__(self, other: Union["Distance", float]) -> bool:
        return self._compare_with_operand(other, operator.lt)

    def __gt__(self, other: Union["Distance", float]) -> bool:
        return self._compare_with_operand(other, operator.gt)

    def __eq__(self, other: Union["Distance", float]) -> bool:
        return self._compare_with_operand(other, operator.eq)

    def __le__(self, other: Union["Distance", float]) -> bool:
        return self._compare_with_operand(other, operator.le)

    def __ge__(self, other: Union["Distance", float]) -> bool:
        return self._compare_with_operand(other, operator.ge)
