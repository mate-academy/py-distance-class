from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)

        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            return Distance(km=self.km * other.real)

    def __truediv__(self, other: Distance) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            return Distance(km=round(self.km / other.real, 2))

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            if self.km < other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km < other.real:
                return True

            return False

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            if self.km > other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km > other.real:
                return True

            return False

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            if self.km == other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km == other.real:
                return True

            return False

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km <= other.real:
                return True

            return False

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km >= other.real:
                return True

            return False
