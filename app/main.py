from typing import Union

types_of_other = Union["Distance", int, float]


class Distance:
    @staticmethod
    def check_arg(arg: types_of_other) -> bool:
        return isinstance(arg, Distance)

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: types_of_other) -> "Distance":
        return Distance(self.km + (other.km
                                   if self.check_arg(other)
                                   else other))

    def __iadd__(self, other: types_of_other) -> "Distance":
        if self.check_arg(other):
            self.km += other.km
        else:
            self.km += other

        return self

    def __mul__(self, number: int | float) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: int) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: types_of_other) -> bool:
        return self.km < (other.km if self.check_arg(other) else other)

    def __gt__(self, other: types_of_other) -> bool:
        return self.km > (other.km if self.check_arg(other) else other)

    def __eq__(self, other: types_of_other) -> bool:
        return self.km == (other.km if self.check_arg(other) else other)

    def __le__(self, other: types_of_other) -> bool:
        return self.km <= (other.km if self.check_arg(other) else other)

    def __ge__(self, other: types_of_other) -> bool:
        return self.km >= (other.km if self.check_arg(other) else other)


# distance = Distance(20)
