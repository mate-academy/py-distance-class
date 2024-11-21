from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: int | float | Distance) -> Distance:
        if isinstance(other_distance, (int, float)):
            return Distance(self.km + other_distance)
        return Distance(self.km + other_distance.km)

    def __iadd__(self, other_distance: int | float | Distance) -> Distance:
        if isinstance(other_distance, (int, float)):
            self.km += other_distance
            return self
        else:
            self.km += other_distance.km
            return self

    def __mul__(self, number: int | float) -> Distance:
        if isinstance(number, (int, float)):
            return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        if isinstance(number, (int, float)):
            return Distance(round(self.km / number, 2))

    def __eq__(self, other_distance: int | float | Distance) -> bool:
        if isinstance(other_distance, Distance):
            return self.km == other_distance.km
        return self.km == other_distance

    def __lt__(self, other_distance: int | float | Distance) -> bool:
        if isinstance(other_distance, Distance):
            return self.km < other_distance.km
        return self.km < other_distance

    def __le__(self, other_distance: int | float | Distance) -> bool:
        return not self > other_distance

    def __gt__(self, other_distance: int | float | Distance) -> bool:
        if isinstance(other_distance, Distance):
            return self.km > other_distance.km
        return self.km > other_distance

    def __ge__(self, other_distance: int | float | Distance) -> bool:
        return not self.km < other_distance
