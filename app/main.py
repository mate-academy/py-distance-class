from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __mul__(self, other: int | float | Distance) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float | Distance) -> Distance:
        return Distance(round((self.km / other), 2))

    @staticmethod
    def get_other_km(other_object: int | float | Distance) -> int | float:
        if isinstance(other_object, Distance):
            return other_object.km
        return other_object

    def __add__(self, other: int | float | Distance) -> Distance:
        return Distance(self.km + Distance.get_other_km(other_object=other))

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += Distance.get_other_km(other_object=other)
        return self

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < Distance.get_other_km(other_object=other)

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > Distance.get_other_km(other_object=other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == Distance.get_other_km(other_object=other)

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= Distance.get_other_km(other_object=other)

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= Distance.get_other_km(other_object=other)
