from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("Pass a number!")
        if km < 0:
            raise ValueError("Pass a positive number!")
        self.km = km

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("Add a Distance object or a number!")

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Add a Distance object or a number!")
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Multiply by 0 or a positive number!")
            return Distance(km=self.km * other)
        raise TypeError("Multiply by a number!")

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError("Divide by positive number!")
            return Distance(km=round(self.km / other, 2))
        raise TypeError("Divide by number!")

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("Compare with a Distance object or a number!")

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        raise TypeError("Compare with a Distance object or a number!")

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        raise TypeError("Compare with a Distance object or a number!")

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError("Compare with a Distance object or a number!")

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError("Compare with a Distance object or a number!")

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
