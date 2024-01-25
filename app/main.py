from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(km=self.km + float(other))
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += float(other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

        return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(km=self.km * float(other))
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __truediv__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Division by zero is not allowed.")
            return Distance(km=round(self.km / float(other), 2))
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < float(other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > float(other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == float(other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __le__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= float(other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __ge__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= float(other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")
