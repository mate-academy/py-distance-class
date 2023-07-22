from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, another: Distance | int) -> Distance:
        if isinstance(another, Distance):
            return Distance(self.km + another.km)

        return Distance(self.km + another)

    def __iadd__(self, another: Distance | int) -> Distance:
        if isinstance(another, Distance):
            self.km += another.km
        else:
            self.km += another

        return self

    def __mul__(self, number: int | float) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        return Distance(round(self.km / number, 2))

    def __lt__(self, another: Distance | int | float) -> bool:
        if isinstance(another, Distance):
            if self.km < another.km:
                return True
            return False

        if self.km < another:
            return True

        return False

    def __gt__(self, another: Distance | int | float) -> bool:
        if isinstance(another, Distance):
            if self.km > another.km:
                return True
            return False

        if self.km > another:
            return True

        return False

    def __eq__(self, another: Distance | int | float) -> bool:
        if isinstance(another, Distance):
            if self.km == another.km:
                return True
            return False

        if self.km == another:
            return True

        return False

    def __le__(self, another: Distance | int | float) -> bool:
        if isinstance(another, Distance):
            if self.km <= another.km:
                return True
            return False

        if self.km <= another:
            return True

        return False

    def __ge__(self, another: Distance | int | float) -> bool:
        if isinstance(another, Distance):
            if self.km >= another.km:
                return True
            return False

        if self.km >= another:
            return True

        return False
