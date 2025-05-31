from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: NumericType) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new: DistanceType) -> Distance:
        if isinstance(new, Distance):
            return Distance(self.km + new.km)
        elif isinstance(new, NumericType):
            return Distance(self.km + new)
        else:
            raise Distance.err(new)

    def __iadd__(self, new: DistanceType) -> Distance:
        if isinstance(new, Distance):
            self.km += new.km
        elif isinstance(new, NumericType):
            self.km += new
        else:
            raise Distance.err(new)
        return self

    def __mul__(self, new: NumericType) -> Distance:
        if isinstance(new, NumericType):
            return Distance(self.km * new)
        else:
            raise Distance.err(new)

    def __truediv__(self, new: DistanceType) -> Distance:
        if isinstance(new, NumericType):
            return Distance(round(self.km / new, 2))
        else:
            raise Distance.err(new)

    def __lt__(self, new: DistanceType) -> bool:
        if isinstance(new, Distance):
            return self.km < new.km
        elif isinstance(new, NumericType):
            return self.km < new
        else:
            raise Distance.err(new)

    def __gt__(self, new: DistanceType) -> bool:
        if isinstance(new, Distance):
            return self.km > new.km
        elif isinstance(new, NumericType):
            return self.km > new
        else:
            raise Distance.err(new)

    def __eq__(self, new: DistanceType) -> bool:
        if isinstance(new, Distance):
            return self.km == new.km
        elif isinstance(new, NumericType):
            return self.km == new
        else:
            raise Distance.err(new)

    def __le__(self, new: DistanceType) -> bool:
        if isinstance(new, Distance):
            return self.km <= new.km
        elif isinstance(new, NumericType):
            return self.km <= new
        else:
            raise Distance.err(new)

    def __ge__(self, new: DistanceType) -> bool:
        if isinstance(new, Distance):
            return self.km >= new.km
        elif isinstance(new, NumericType):
            return self.km >= new
        else:
            raise Distance.err(new)

    @staticmethod
    def err(new: Any) -> TypeError:
        return TypeError(f"Error type: {type(new).__name__} is not valid")


DistanceType = Distance | int | float
NumericType = int | float
