from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: any) -> Distance:
        if isinstance(other_distance, (int, float)):
            self.km = self.km + other_distance
        else:
            self.km = self.km + other_distance.km
        return Distance(self.km)

    def __iadd__(self, other_distance: any) -> Distance:
        if isinstance(other_distance, (int, float)):
            self.km += other_distance
        elif isinstance(other_distance, Distance):
            self.km += other_distance.km
        return self

    def __mul__(self, number: any) -> Distance:
        self.km = self.km * number
        return Distance(self.km)

    def __truediv__(self, number: any) -> Distance:
        self.km = round(self.km / number, 2)
        return Distance(self.km)

    def __lt__(self, other_distance: any) -> bool:
        if isinstance(other_distance, (int, float)):
            return self.km < other_distance
        return self.km < other_distance.km

    def __gt__(self, other_distance: any) -> bool:
        if isinstance(other_distance, (int, float)):
            return self.km > other_distance
        return self.km > other_distance.km

    def __eq__(self, other_distance: any) -> bool:
        if isinstance(other_distance, (int, float)):
            return self.km == other_distance
        return self.km == other_distance.km

    def __le__(self, other_distance: any) -> bool:
        if isinstance(other_distance, (int, float)):
            return self.km <= other_distance
        return self.km <= other_distance.km

    def __ge__(self, other_distance: any) -> bool:
        if isinstance(other_distance, (int, float)):
            return self.km >= other_distance
        return self.km >= other_distance.km
