from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(
            f"Wrong type of '{other}'."
            f"Should be 'Distance', 'int' or 'float'"
        )

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        elif isinstance(other, (int, float)):
            self.km = self.km + other
            return self
        raise TypeError(
            f"Wrong type of '{other}'."
            f"Should be 'Distance', 'int' or 'float'"
        )

    def __mul__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
            f"Wrong type of '{other}'."
            f"Should be 'int' or 'float'"
        )

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError(
            f"Wrong type of '{other}'."
            f"Should be 'int' or 'float'"
        )

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return True if self.km < other.km else False
        elif isinstance(other, (int, float)):
            return True if self.km < other else False
        raise TypeError(
            f"Wrong type of '{other}'."
            f"Should be 'Distance', 'int' or 'float'"
        )

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return True if self.km > other.km else False
        elif isinstance(other, (int, float)):
            return True if self.km > other else False
        raise TypeError(
            f"Wrong type of '{other}'."
            f"Should be 'Distance', 'int' or 'float'"
        )

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return True if self.km == other.km else False
        elif isinstance(other, (int, float)):
            return True if self.km == other else False
        raise TypeError(
            f"Wrong type of '{other}'."
            f"Should be 'Distance', 'int' or 'float'"
        )

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return True if self.km <= other.km else False
        elif isinstance(other, (int, float)):
            return True if self.km <= other else False
        raise TypeError(
            f"Wrong type of '{other}'."
            f"Should be 'Distance', 'int' or 'float'"
        )

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return True if self.km >= other.km else False
        elif isinstance(other, (int, float)):
            return True if self.km >= other else False
        raise TypeError(
            f"Wrong type of '{other}'."
            f"Should be 'Distance', 'int' or 'float'"
        )
