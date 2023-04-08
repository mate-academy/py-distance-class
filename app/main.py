from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"

    def __add__(self, distance2: Distance | int | float) -> Distance:
        if isinstance(distance2, (int, float)):
            return Distance(self.km + distance2)
        elif isinstance(distance2, Distance):
            return Distance(self.km + distance2.km)
        else:
            raise TypeError

    def __iadd__(self, distance2: Distance | int | float) -> Distance:
        if isinstance(distance2, (int, float)):
            self.km += distance2
        elif isinstance(distance2, Distance):
            self.km += distance2.km
        else:
            raise TypeError

        return self

    def __mul__(self, distance2: int | float) -> Distance:
        return Distance(self.km * distance2)

    def __truediv__(self, distance2: int | float) -> Distance:
        return Distance(round(self.km / distance2, 2))

    def __eq__(self, distance2: Distance | int | float) -> bool:
        if isinstance(distance2, (int, float)):
            return self.km == distance2
        elif isinstance(distance2, Distance):
            return self.km == distance2.km
        else:
            raise TypeError

    def __lt__(self, distance2: Distance | int | float) -> bool:
        if isinstance(distance2, (int, float)):
            return self.km < distance2
        elif isinstance(distance2, Distance):
            return self.km < distance2.km
        else:
            raise TypeError

    def __gt__(self, distance2: Distance | int | float) -> bool:
        if isinstance(distance2, (int, float)):
            return self.km > distance2
        elif isinstance(distance2, Distance):
            return self.km > distance2.km
        else:
            raise TypeError

    def __le__(self, distance2: Distance | int | float) -> bool:
        if isinstance(distance2, (int, float)):
            return self.km <= distance2
        elif isinstance(distance2, Distance):
            return self.km <= distance2.km
        else:
            raise TypeError

    def __ge__(self, distance2: Distance | int | float) -> bool:
        if isinstance(distance2, (int, float)):
            return self.km >= distance2
        elif isinstance(distance2, Distance):
            return self.km >= distance2.km
        else:
            raise TypeError
