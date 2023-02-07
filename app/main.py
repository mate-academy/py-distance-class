from __future__ import annotations


class Distance:
    def __init__(self, km: [float | int]) -> Distance:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: [Distance | float | int]) -> Distance:
        if isinstance(other_distance, int | float):
            return Distance(self.km + other_distance)
        return Distance(self.km + other_distance.km)

    def __iadd__(self, other_distance: [Distance | float | int]) -> Distance:
        if isinstance(other_distance, int | float):
            self.km = self.km + other_distance
        else:
            self.km = self.km + other_distance.km
        return self

    def __mul__(self, multiplier: [float | int]) -> Distance:
        return Distance(self.km * multiplier)

    def __truediv__(self, divider: [float | int]) -> Distance:
        return Distance(round(self.km / divider, 2))

    def __lt__(self, other_distance: [Distance | float | int]) -> bool:
        if isinstance(other_distance, int | float):
            return self.km < other_distance
        return self.km < other_distance.km

    def __gt__(self, other_distance: [Distance | float | int]) -> bool:
        if isinstance(other_distance, int | float):
            return self.km > other_distance
        return self.km > other_distance.km

    def __eq__(self, other_distance: [Distance | float | int]) -> bool:
        if isinstance(other_distance, int | float):
            return self.km == other_distance
        return self.km == other_distance.km

    def __le__(self, other_distance: [Distance | float | int]) -> bool:
        if isinstance(other_distance, int | float):
            return self.km <= other_distance
        return self.km <= other_distance.km

    def __ge__(self, other_distance: [Distance | float | int]) -> bool:
        if isinstance(other_distance, int | float):
            return self.km >= other_distance
        return self.km >= other_distance.km
