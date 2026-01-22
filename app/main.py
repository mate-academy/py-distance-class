from __future__ import annotations
class Distance:
    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" | int | float) -> "Distance" | int | float:
        other_km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + other_km)

    def __mul__(self, other: int) -> "Distance":
        new_num = self.km * other
        return Distance(new_num)

    def __iadd__(self, other: int) -> "Distance":
        other_km = other.km if isinstance(other, Distance) else other
        self.km += other_km
        return self

    def __truediv__(self, other: int) -> "Distance":
        new_num = round(self.km / other, 2)
        return Distance(new_num)

    def __lt__(self, other: "Distance" | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other: "Distance" | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other: "Distance" | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km == other_km

    def __le__(self, other: "Distance" | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other: "Distance" | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
