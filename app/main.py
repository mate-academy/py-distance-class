from __future__ import annotations

from typing import Union


class Distance:

    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: str) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise ValueError("Can only add Distance objects or numbers")

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise ValueError("Can only add Distance objects or numbers")
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (Distance)):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise ValueError("Can only compare Distance objects or numbers")

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (Distance)):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise ValueError("Can only compare Distance objects or numbers")

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (Distance)):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise ValueError("Can only compare Distance objects or numbers")

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (Distance)):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise ValueError("Can only compare Distance objects or numbers")

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (Distance)):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise ValueError("Can only compare Distance objects or numbers")
