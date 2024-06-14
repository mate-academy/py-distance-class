from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"unsupported operand type for +: {type(other)}")

        return Distance(
            km=self.km + (other.km if isinstance(other, Distance) else other)
        )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"unsupported operand type for +: {type(other)}")

        self.km += (other.km if isinstance(other, Distance) else other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(f"unsupported operand type for +: {type(other)}")

        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(f"unsupported operand type for +: {type(other)}")

        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"unsupported operand type for +: {type(other)}")

        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"unsupported operand type for +: {type(other)}")

        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"unsupported operand type for +: {type(other)}")

        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"unsupported operand type for +: {type(other)}")

        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"unsupported operand type for +: {type(other)}")

        return self.km >= (other.km if isinstance(other, Distance) else other)
