from typing import Any


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        return Distance(km=self.km + other)

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        self.km = self.km + other
        return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(km=self.km * other)

    def __truediv__(self, other: int) -> "Distance":
        if other != 0:
            res_km = round((self.km / other), 2)
        return Distance(km=res_km)

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Any) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km >= other
        return self.km >= other.km


# distance = Distance(20)
# print(distance)
# print(repr(distance))
# distance1 = Distance(30)
# distance2 = distance1 + distance
# print(distance2.km)
# distance3 = distance + 10
# print(distance3.km)
# res = distance
# distance += distance1
# print()
# distance += 30
# print(distance)
#
