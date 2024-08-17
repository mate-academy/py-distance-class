from __future__ import annotations


class Distance:

    @staticmethod
    def other_isinstance(other: object) -> object:
        if isinstance(other, (int, float)):
            return other
        else:
            return other.km

    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> Distance:
        return Distance(self.km + Distance.other_isinstance(other))

    def __iadd__(self, other: object) -> Distance:
        self.km += Distance.other_isinstance(other)
        return self

    def __mul__(self, other: object) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: object) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: object) -> bool:
        return self.km < Distance.other_isinstance(other)

    def __gt__(self, other: object) -> bool:
        return self.km > Distance.other_isinstance(other)

    def __eq__(self, other: object) -> bool:
        return self.km == Distance.other_isinstance(other)

    def __le__(self, other: object) -> bool:
        return self.km <= Distance.other_isinstance(other)

    def __ge__(self, other: object) -> bool:
        return self.km >= Distance.other_isinstance(other)
