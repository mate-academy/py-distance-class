from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, second: Distance | int | float) -> Distance:
        if isinstance(second, Distance):
            return Distance(km=self.km + second.km)
        return Distance(km=self.km + second)

    def __iadd__(self, second: Distance | int | float) -> Distance:
        if isinstance(second, Distance):
            self.km = self.km + second.km
        else:
            self.km = self.km + second
        return self

    def __mul__(self, second: int | float) -> Distance:
        return Distance(km=self.km * second)

    def __truediv__(self, second: int | float) -> Distance:
        return Distance(km=round(self.km / second, 2))

    def __lt__(self, second: Distance | int | float) -> bool:
        if isinstance(second, Distance):
            return self.km < second.km
        return self.km < second

    def __gt__(self, second: Distance | int | float) -> bool:
        if isinstance(second, Distance):
            return self.km > second.km
        return self.km > second

    def __eq__(self, second: Distance | int | float) -> bool:
        if isinstance(second, Distance):
            return self.km == second.km
        return self.km == second

    def __le__(self, second: Distance | int | float) -> bool:
        if isinstance(second, Distance):
            return self.km <= second.km
        return self.km <= second

    def __ge__(self, second: Distance | int | float) -> bool:
        if isinstance(second, Distance):
            return self.km >= second.km
        return self.km >= second
