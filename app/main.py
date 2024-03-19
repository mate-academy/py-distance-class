from __future__ import annotations

import operator


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance | TypeError:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

        raise TypeError("Unsupported operand for addition")

    def __iadd__(self, other: int | float | Distance) -> Distance | TypeError:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +=: /n"
                f" 'Distance' and '{type(other)}'"
            )
        return self

    def __mul__(self, other: int | float) -> Distance | TypeError:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        elif isinstance(other, Distance):
            raise TypeError("Unsupported operation.")

    def __truediv__(self, other: int | float) -> Distance | TypeError:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        elif isinstance(other, Distance):
            raise TypeError("Unsupported operation.")

    def __lt__(self, other: int | float) -> bool | TypeError:
        return self._compare_with_operand(other, operator.lt)

    def __gt__(self, other: int | float) -> bool | TypeError:
        return self._compare_with_operand(other, operator.gt)

    def __eq__(self, other: int | float) -> bool:
        return self._compare_with_operand(other, operator.eq)

    def __ge__(self, other: int | float) -> bool | TypeError:
        return self._compare_with_operand(other, operator.ge)

    def __le__(self, other: int | float) -> bool | TypeError:
        return self._compare_with_operand(other, operator.le)

    def _compare_with_operand(
            self,
            other: Distance | float,
            comparison_operator: callable
    ) -> bool | TypeError:
        if isinstance(other, Distance):
            return comparison_operator(self.km, other.km)
        elif isinstance(other, (int, float)):
            return comparison_operator(self.km, other)
        else:
            raise TypeError("Unsupported type for comparison.")
