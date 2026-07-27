from typing import Any


class Distance:

    def __init__(self, distance: float) -> None:
        self.km = distance

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, float) or isinstance(other, int):
            return Distance(self.km + other)

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (float, int)):
            self.km += other
        return self

    def __mul__(self, other: Any) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(self.km * other)
        else:
            raise TypeError(
                "Multiplication is only supported with "
                "float or int types."
            )

    def __truediv__(self, other: Any) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError(
                "Division is only supported with "
                "float or int types."
            )

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (float, int)):
            return self.km < other
        else:
            raise TypeError(
                "Comparison is only supported with "
                "Distance, float or int types."
            )

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (float, int)):
            return self.km > other
        else:
            raise TypeError(
                "Comparison is only supported with "
                "Distance, float or int types."
            )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (float, int)):
            return self.km == other
        else:
            raise TypeError(
                "Comparison is only supported with "
                "Distance, float or int types."
            )

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (float, int)):
            return self.km <= other
        else:
            raise TypeError(
                "Comparison is only supported with "
                "Distance, float or int types."
            )

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (float, int)):
            return self.km >= other
        else:
            raise TypeError(
                "Comparison is only supported with "
                "Distance, float or int types."
            )
