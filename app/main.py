from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return None

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return None
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            return None

    def __truediv__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            result = self.km / other
            return Distance(round(result, 2))
        else:
            return None

    def comparison(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return self.km - other.km
        elif isinstance(other, (int, float)):
            return self.km - other
        else:
            return None

    def __lt__(self, other: int) -> bool:
        return self.comparison(other) < 0

    def __gt__(self, other: int) -> bool:
        return self.comparison(other) > 0

    def __eq__(self, other: int) -> bool:
        return self.comparison(other) == 0

    def __le__(self, other: int) -> bool:
        return self.comparison(other) <= 0

    def __ge__(self, other: int) -> bool:
        return self.comparison(other) >= 0
