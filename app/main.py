from __future__ import annotations


class Distance:
    def __init__(self, km) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            distance_to_add = other.km
        else:
            distance_to_add = other
        return Distance(
            self.km + distance_to_add
        )

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            distance_to_add = other.km
        else:
            distance_to_add = other
        self.km += distance_to_add
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int) -> Distance:
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            distance_to_compare = other.km
        else:
            distance_to_compare = other
        if self.km < distance_to_compare:
            return True
        else:
            return False

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            distance_to_compare = other.km
        else:
            distance_to_compare = other
        if self.km > distance_to_compare:
            return True
        else:
            return False

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            distance_to_compare = other.km
        else:
            distance_to_compare = other
        if self.km == distance_to_compare:
            return True
        else:
            return False

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            distance_to_compare = other.km
        else:
            distance_to_compare = other
        if self.km <= distance_to_compare:
            return True
        else:
            return False

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            distance_to_compare = other.km
        else:
            distance_to_compare = other
        if self.km >= distance_to_compare:
            return True
        else:
            return False
