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
            new_km = self.km + other.km
        elif isinstance(other, (int, float)):
            new_km = self.km + other
        else:
            raise TypeError("unsupported operand type(s) for +: 'Distance'")
        return Distance(new_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("unsupported operand type(s) for +: 'Distance'")
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            new_km = self.km * other
        else:
            raise TypeError("unsupported operand type(s) for +: 'Distance'")
        return Distance(new_km)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)) and other != 0:
            new_km = self.km / other
        else:
            raise TypeError("unsupported operand type(s) for +: 'Distance'")
        return Distance(round(new_km, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("unsupported operand type(s) for +: 'Distance'")

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("unsupported operand type(s) for +: 'Distance'")

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("unsupported operand type(s) for +: 'Distance'")

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("unsupported operand type(s) for +: 'Distance'")

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("unsupported operand type(s) for +: 'Distance'")
