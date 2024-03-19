from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @property
    def km(self) -> int | float:
        return self._km

    @km.setter
    def km(self, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError(
                f"Unsupported type. <class 'float'> "
                f"or <class 'int'> were expected. "
                f"Got {type(value)} instead."
            )
        self._km = value

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            other = Distance(other)
        self.km += other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            other = Distance(other)
            return Distance(self.km * other.km)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            other = Distance(other)
            return Distance(round(self.km / other.km, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return self.km < other.km

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return self.km > other.km

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return self.km == other.km

    def __le__(self, other: int | float | Distance) -> bool:
        return not self > other

    def __ge__(self, other: int | float | Distance) -> bool:
        return not self < other
