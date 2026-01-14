from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(
            self,
            another: Distance | int | float
    ) -> Distance:
        if isinstance(another, Distance):
            return Distance(km=self.km + another.km)
        return Distance(km=self.km + another)

    def __iadd__(
            self,
            another: Distance | int | float
    ) -> Distance:
        if isinstance(another, Distance):
            self.km += another.km
        else:
            self.km += another
        return self

    def __mul__(
            self,
            another: int | float
    ) -> Distance:
        return Distance(km=self.km * another)

    def __truediv__(
            self,
            another: int | float
    ) -> Distance:
        return Distance(km=round(self.km / another, 2))

    def __lt__(
            self,
            another: Distance | int | float
    ) -> bool:
        if isinstance(another, Distance):
            return self.km < another.km
        return self.km < another

    def __gt__(
            self,
            another: Distance | int | float
    ) -> bool:
        if isinstance(another, Distance):
            return self.km > another.km
        return self.km > another

    def __eq__(
            self,
            another: Distance | int | float
    ) -> bool:
        if isinstance(another, Distance):
            return self.km == another.km
        return self.km == another

    def __le__(
            self,
            another: Distance | int | float
    ) -> bool:
        if isinstance(another, Distance):
            return self.km <= another.km
        return self.km <= another

    def __ge__(
            self,
            another: Distance | int | float
    ) -> bool:
        if isinstance(another, Distance):
            return self.km >= another.km
        return self.km >= another
