from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError(
                "Unsupported type for addition. "
                "Expected Distance, int or float."
            )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                "Unsupported type for equality comparison. "
                "Expected Distance, int or float."
            )
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError(
                "Unsupported type for multiplication. "
                "Expected int or float."
            )

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError(
                "Unsupported type for division. "
                "Expected int or float."
            )

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError(
                "Unsupported type for equality comparison. "
                "Expected Distance, int or float."
            )

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError(
                "Unsupported type for equality comparison. "
                "Expected Distance, int or float."
            )

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError(
                "Unsupported type for equality comparison. "
                "Expected Distance, int or float."
            )

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return not self.km > other.km
        elif isinstance(other, (int, float)):
            return not self > other
        else:
            raise TypeError(
                "Unsupported type for less-than-or-equal comparison. "
                "Expected Distance, int or float."
            )

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return not self.km < other.km
        elif isinstance(other, (int, float)):
            return not self.km < other
        else:
            raise TypeError(
                "Unsupported type for greater-than-or-equal comparison. "
                "Expected Distance, int or float."
            )
