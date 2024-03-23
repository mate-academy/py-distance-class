from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    @staticmethod
    def validator(
            other: Union["Distance", int, float],
            *numeric_types,
            distance: "Distance" = None
    ) -> Union["Distance", int, float]:
        if numeric_types and not isinstance(other, (numeric_types, distance)):
            raise TypeError(
                "Operator must be of a Distance instance or number"
            )

        if distance and isinstance(other, Distance):
            return other.km

        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        return Distance(self.km + self.validator(
            other, int, float, distance=Distance
        ))

    def __iadd__(self, other: "Distance") -> "Distance":
        self.km += self.validator(other, distance=Distance)
        return self

    def __mul__(self, other: "Distance") -> "Distance":
        return Distance(self.km * self.validator(other, int, float))

    def __truediv__(self, other: "Distance") -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance") -> bool:
        return self.km < other

    def __gt__(self, other: "Distance") -> bool:
        return self.km > other

    def __eq__(self, other: "Distance") -> bool:
        return self.km == other

    def __le__(self, other: "Distance") -> bool:
        return self.km <= self.validator(other, int, float, distance=Distance)

    def __ge__(self, other: "Distance") -> bool:
        return self.km >= self.validator(other, int, float, distance=Distance)
