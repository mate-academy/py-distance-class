from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        if self.km == int(self.km):
            km_str = str(int(self.km))
        else:
            km_str = str(self.km)
        return f"Distance: {km_str} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        if (not isinstance(other, (int, float))
                and not isinstance(other, Distance)):
            raise TypeError()

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, (int, float)):
            self.km += other
        if (not isinstance(other, Distance)
                and not isinstance(other, (int, float))):
            raise TypeError()
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        if not isinstance(other, (int, float)):
            raise TypeError()

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Distance(round(self.km / other, 2))
        if not isinstance(other, (int, float)):
            raise TypeError()

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        if (not isinstance(other, Distance)
                and isinstance(other, (int, float))):
            raise TypeError()

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        if (not isinstance(other, Distance)
                and not isinstance(other, (int, float))):
            raise TypeError()

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        if (not isinstance(other, Distance)
                and isinstance(other, (int, float))):
            return False

    def __le__(self, other: Distance | int | float) -> bool:
        return self < other or self == other

    def __ge__(self, other: Distance | int | float) -> bool:
        return self > other or self == other
