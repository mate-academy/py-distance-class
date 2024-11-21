from typing import Union

types_of_other = Union["Distance", int, float]


class Distance:
    @staticmethod
    def check_arg(other: types_of_other) -> bool:
        return isinstance(other, Distance)

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: types_of_other) -> "Distance":
        check_type_of_other = other.km if self.check_arg(other) else other

        return Distance(self.km + check_type_of_other)

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
        check_type_of_other = other.km if self.check_arg(other) else other

        return self.km < check_type_of_other

    def __gt__(self, other: types_of_other) -> bool:
        check_type_of_other = other.km if self.check_arg(other) else other

        return self.km > check_type_of_other

    def __eq__(self, other: types_of_other) -> bool:
        check_type_of_other = other.km if self.check_arg(other) else other

        return self.km == check_type_of_other

    def __le__(self, other: types_of_other) -> bool:
        check_type_of_other = other.km if self.check_arg(other) else other

        return self.km <= check_type_of_other

    def __ge__(self, other: types_of_other) -> bool:
        check_type_of_other = other.km if self.check_arg(other) else other

        return self.km >= check_type_of_other
