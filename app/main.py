from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" | int | float) -> "Distance":
        if isinstance(other, Distance):
            distance = self.km + other.km
            return Distance(distance)
        if isinstance(other, (int, float)):
            distance = self.km + other
            return Distance(distance)
        raise TypeError(f"Cannot add {type(other)} distance to {type(self)}")

    def __iadd__(self, other: "Distance" | int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        raise TypeError(f"Cannot add {type(other)} distance to {type(self)}")

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            distance = self.km * other
            return Distance(distance)
        raise TypeError(f"Cannot add {type(other)} distance to {type(self)}")

    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            distance = self.km / other
            return Distance(round(distance, 2))
        raise TypeError(f"Cannot add {type(other)} distance to {type(self)}")

    def __lt__(self, other: "Distance" | int | float) -> bool | None:
        if isinstance(other, (int, float)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km
        raise TypeError(f"Cannot add {type(other)} distance to {type(self)}")

    def __gt__(self, other: "Distance" | int | float) -> bool | None:
        if isinstance(other, (int, float)):
            return self.km > other
        if isinstance(other, Distance):
            return self.km > other.km
        raise TypeError(f"Cannot add {type(other)} distance to {type(self)}")

    def __eq__(self, other: "Distance" | int | float) -> bool | None:
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km
        raise TypeError(f"Cannot add {type(other)} distance to {type(self)}")

    def __le__(self, other: "Distance" | int | float) -> bool | None:
        if isinstance(other, (int, float)):
            return self.km <= other
        if isinstance(other, Distance):
            return self.km <= other.km
        raise TypeError(f"Cannot add {type(other)} distance to {type(self)}")

    def __ge__(self, other: "Distance" | int | float) -> bool | None:
        if isinstance(other, (int, float)):
            return self.km >= other
        if isinstance(other, Distance):
            return self.km >= other.km
        raise TypeError(f"Cannot add {type(other)} distance to {type(self)}")
