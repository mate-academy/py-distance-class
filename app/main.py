from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):  # Перевірка на число
            return Distance(self.km + other)
        if isinstance(other, Distance):  # Перевірка на Distance
            return Distance(self.km + other.km)
        else:  # Обробка невідповідного типу
            raise TypeError(f"Unsupported operand type(s) "
                            f"for +: 'Distance' and '{type(other).__name__}'"
                            )

    def __iadd__(self, other: (int, float, Distance)) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        if isinstance(other, Distance):
            self.km += other.km
            return self

    def __mul__(self, other: int) -> Distance:
        if isinstance(other, (int, float)):  # Перевірка на число
            return Distance(self.km * other)
        raise TypeError("Unsupported operand type(s) for *:"
                        " 'Distance' and '{}'".format(type(other).__name__)
                        )

    def __truediv__(self, other: int) -> Distance:
        if isinstance(other, (int, float)):  # Перевірка на число
            if other == 0:  # Додано перевірку на ділення на нуль
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Distance(round(self.km / other, 2))
        raise TypeError("Unsupported operand type(s) for /: "
                        "'Distance' and '{}'".format(type(other).__name__)
                        )

    def __lt__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km

    def __gt__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        if isinstance(other, Distance):
            return self.km > other.km

    def __eq__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km

    def __le__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        if isinstance(other, Distance):
            return self.km <= other.km

    def __ge__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        if isinstance(other, Distance):
            return self.km >= other.km
