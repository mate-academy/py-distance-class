from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance | int | float):
            raise TypeError(f"You can't add {type(other)} to class Distance")
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)

        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance | int | float):
            raise TypeError(f"You can't add {type(other)} to class Distance")
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        if not isinstance(other, int | float):
            raise TypeError(f"You can't multiply {type(other)} "
                            f"on class Distance")
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, int | float):
            raise TypeError(f"You can't divide class Distance "
                            f"by {type(other)}")
        return Distance(km=round((self.km / other), 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance | int | float):
            raise TypeError(f"You can't compare {type(other)} "
                            f"and class Distance")
        if isinstance(other, Distance):
            return self.km < other.km

        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance | int | float):
            raise TypeError(f"You can't compare {type(other)} "
                            f"and class Distance")
        if isinstance(other, Distance):
            return self.km > other.km

        return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance | int | float):
            raise TypeError(f"You can't compare {type(other)} "
                            f"and class Distance")
        if isinstance(other, Distance):
            return self.km == other.km

        return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        return self < other or self == other

    def __ge__(self, other: Distance | int | float) -> bool:
        return self > other or self == other
