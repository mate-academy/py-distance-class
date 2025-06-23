from typing import Union


class Distance:

    def __init__(self, km: float) -> None:
        self.km = float(km)

    def __str__(self) -> str:
        if self.km == int(self.km):
            return f"Distance: {int(self.km)} kilometers."
        else:
            return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        if self.km == int(self.km):
            return f"Distance(km={int(self.km)})"
        else:
            return f"Distance(km={self.km})"

    def __add__(self, other: Union[float, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        else:
            return Distance(
                km=self.km + float(other)
            )

    def __iadd__(self, other: Union["Distance", float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += float(other)
        return self

    def __mul__(self, other: float) -> "Distance":
        return Distance(round(self.km * other, 3))

    def __truediv__(self, other: float) -> "Distance":
        return Distance(round(self.km / float(other), 2))
        # isinstance(distance2, Distance) is True
    # distance2.km == 2.85
    # Note: rounded to 2 decimals

    def __lt__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < float(other)

    def __gt__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > float(other)

    def __eq__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == float(other)

    def __le__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= float(other)

    def __ge__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= float(other)
