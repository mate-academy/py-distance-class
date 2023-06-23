from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __float__(self) -> float:
        return float(self.km)

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + float(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += float(other)
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        new_distance = round(self.km / other, 2)
        return Distance(new_distance)

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < float(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > float(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == float(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= float(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= float(other)
