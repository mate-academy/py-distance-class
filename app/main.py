from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> callable:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for +: 'Distance' and '{}'".format(type(other)))

    def __iadd__(self, other: int | float | Distance) -> callable:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for +=: 'Distance' and '{}'".format(type(other)))
        return self

    def __mul__(self, scalar: int | float) -> callable:
        return Distance(self.km * scalar)

    def __truediv__(self, scalar: int | float) -> callable:
        return Distance(round(self.km / scalar, 2))

    def __lt__(self, other: int | float | Distance) -> callable:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for <: 'Distance' and '{}'".format(type(other)))

    def __gt__(self, other: int | float | Distance) -> callable:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for >: 'Distance' and '{}'".format(type(other)))

    def __eq__(self, other: int | float | Distance) -> int | str:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for ==: 'Distance' and '{}'".format(type(other)))

    def __le__(self, other: int | float | Distance) -> int | float | str:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for <=: 'Distance' and '{}'".format(type(other)))

    def __ge__(self, other: int | float | Distance) -> callable:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for >=: 'Distance' and '{}'".format(type(other)))
