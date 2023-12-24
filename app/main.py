from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        second_operand = (
            other.km
            if isinstance(other, Distance)
            else
            other
        )
        return Distance(
            self.km + second_operand
        )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        second_operand = (
            other.km
            if isinstance(other, Distance)
            else
            other
        )
        self.km += second_operand
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        result = self.km / other
        return Distance(
            round(result, 2)
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        second_operand = (
            other.km
            if isinstance(other, Distance)
            else
            other
        )
        return self.km < second_operand

    def __gt__(self, other: Distance | int | float) -> bool:
        second_operand = (
            other.km
            if isinstance(other, Distance)
            else
            other
        )
        return self.km > second_operand

    def __eq__(self, other: Distance | int | float) -> bool:
        second_operand = (
            other.km
            if isinstance(other, Distance)
            else
            other
        )
        return self.km == second_operand

    def __le__(self, other: Distance | int | float) -> bool:
        second_operand = (
            other.km
            if isinstance(other, Distance)
            else
            other
        )
        return self.km <= second_operand

    def __ge__(self, other: Distance | int | float) -> bool:
        second_operand = (
            other.km
            if isinstance(other, Distance)
            else
            other
        )
        return self.km >= second_operand
