from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new: int | float | Distance) -> Distance:
        if isinstance(new, (int, float)):
            return Distance(self.km + new)
        elif isinstance(new, Distance):
            return Distance(self.km + new.km)

    def __iadd__(self, new: int | float | Distance) -> None:
        if isinstance(new, (int, float)):
            self.km += new
        elif isinstance(new, Distance):
            self.km += new.km
        return self

    def __mul__(self, new: int) -> Distance:
        res = self.km * new
        return Distance(res)

    def __truediv__(self, new: int) -> Distance:
        return Distance(round(self.km / new, 2))

    def __eq__(self, new: int) -> bool:
        return self.km == new

    def __lt__(self, new: int) -> bool:
        return self.km < new

    def __gt__(self, new: int) -> bool:
        return self.km > new

    def __le__(self, new: int) -> bool:
        return self.km <= new

    def __ge__(self, new: int) -> bool:
        return self.km >= new
