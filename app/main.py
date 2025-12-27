from __future__ import annotations


class Distance:
    def __init__(
            self,
            km: int | float
    ) -> None:
        self.km = km

    @staticmethod
    def other_type_check(other: Distance | float | int) -> bool:
        if not isinstance(other, (Distance, float, int)):
            raise TypeError("'other' is not 'Distance', 'float', 'int'!!!")
        return isinstance(other, Distance)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        return (
            Distance(self.km + other.km)
            if self.other_type_check(other) else
            Distance(self.km + other)
        )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if self.other_type_check(other):
            self.km = self.km + other.km
        elif isinstance(other, (float, int)):
            self.km = self.km + other

        return self

    def __mul__(self, other: float | int) -> Distance:
        if not self.other_type_check(other):
            return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        if not self.other_type_check(other):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        return (
            self.km < other.km
            if self.other_type_check(other) else
            self.km < other
        )

    def __gt__(self, other: Distance | float | int) -> bool:
        return (
            self.km > other.km
            if self.other_type_check(other) else
            self.km > other
        )

    def __eq__(self, other: Distance | float | int) -> bool:
        return (
            self.km == other.km
            if self.other_type_check(other) else
            self.km == other
        )

    def __le__(self, other: Distance | float | int) -> bool:
        return (
            self.km <= other.km
            if self.other_type_check(other) else
            self.km <= other
        )

    def __ge__(self, other: Distance | float | int) -> bool:
        return (
            self.km >= other.km
            if self.other_type_check(other) else
            self.km >= other
        )
