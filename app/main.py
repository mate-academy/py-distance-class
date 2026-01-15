from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def get_km(obj: Distance | float | int) -> float | int:
        return obj.km if isinstance(obj, Distance) else obj

    def __add__(self, other: Distance | float | int) -> Distance:
        return Distance(km=self.km + self.get_km(obj=other))

    def __iadd__(self, other: Distance | float | int) -> Distance:
        self.km += self.get_km(obj=other)
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        return self.km < self.get_km(obj=other)

    def __gt__(self, other: Distance | float | int) -> bool:
        return self.km > self.get_km(obj=other)

    def __eq__(self, other: Distance | float | int) -> bool:
        return self.km == self.get_km(obj=other)

    def __le__(self, other: Distance | float | int) -> bool:
        return not self.__gt__(other=other)

    def __ge__(self, other: Distance | float | int) -> bool:
        return not self.__lt__(other=other)
