from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self. km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_d: Distance | int | float) -> Distance:
        if isinstance(other_d, (int, float)):
            return Distance(km=self.km + other_d)
        return Distance(km=self.km + other_d.km)

    def __iadd__(self, other_d: Distance | int | float) -> Distance:
        if isinstance(other_d, (int, float)):
            self.km += other_d
        else:
            self.km += other_d.km
        return self

    def __mul__(self, multiply: int | float) -> Distance:
        return Distance(km=self.km * multiply)

    def __truediv__(self, number: int | float) -> Distance:
        if isinstance(number, (int, float)):
            if number == 0:
                raise ValueError("Cannot divide by zero.")
            return Distance(km=round((self.km / number), 2))
        raise TypeError

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __le__(self, other: Distance | int | float) -> bool:
        return self < other or self == other

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        return self > other or self == other
