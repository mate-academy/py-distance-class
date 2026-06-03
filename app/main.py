from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            kilometers_to_add = other.km
        else:
            kilometers_to_add = other
        return Distance(self.km + kilometers_to_add)

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            kilometers_to_add = other.km
        else:
            kilometers_to_add = other
        self.km += kilometers_to_add
        return self

    def __mul__(self, other: Distance | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            kilometers_to_compare = other.km
        else:
            kilometers_to_compare = other
        return self.km < kilometers_to_compare

    def __gt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            kilometers_to_compare = other.km
        else:
            kilometers_to_compare = other
        return self.km > kilometers_to_compare

    def __eq__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            kilometers_to_compare = other.km
        else:
            kilometers_to_compare = other
        return self.km == kilometers_to_compare

    def __le__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            kilometers_to_compare = other.km
        else:
            kilometers_to_compare = other
        return self.km <= kilometers_to_compare

    def __ge__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            kilometers_to_compare = other.km
        else:
            kilometers_to_compare = other
        return self.km >= kilometers_to_compare
