from typing import Any


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int | float):
            return Distance(self.km + other)
        else:
            raise (
                TypeError(
                    "Unsupported operand type(s) for +: 'Distance' and 'int'"
                ))

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, int | float):
            self.km += other
            return self
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            raise (
                TypeError(
                    "Unsupported operand type(s) for +: 'Distance' and 'int'"
                ))

    def __mul__(self, number: float) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: float) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int | float):
            return self.km < other
        else:
            raise (
                TypeError(
                    "Unsupported operand type(s) for +: 'Distance' and 'int'"
                ))

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int | float):
            return self.km > other
        else:
            raise (
                TypeError(
                    "Unsupported operand type(s) for +: 'Distance' and 'int'"
                ))

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int | float):
            return self.km == other
        else:
            raise (
                TypeError(
                    "Unsupported operand type(s) for +: 'Distance' and 'int'"
                ))

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int | float):
            return self.km <= other
        else:
            raise (
                TypeError(
                    "Unsupported operand type(s) for +: 'Distance' and 'int'"
                ))

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int | float):
            return self.km >= other
        else:
            raise (
                TypeError(
                    "Unsupported operand type(s) for +: 'Distance' and 'int'"
                ))
