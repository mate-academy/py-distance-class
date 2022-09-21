from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> Distance:
        if isinstance(other, Distance):
            new_distance = self.km + other.km
        else:
            new_distance = self.km + other
        return Distance(new_distance)

    def __radd__(self, other) -> Distance:
        if isinstance(other, Distance):
            new_distance = other.km + self.km
        else:
            new_distance = other + self.km
        return Distance(new_distance)

    def __iadd__(self, other) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int) -> Distance:
        self.km *= other
        return Distance(self.km)

    def __truediv__(self, other) -> Distance:
        self.km /= other
        return Distance(round(self.km, 2))

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return other == self.km

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return other > self.km

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return other < self.km

    def __le__(self, other) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other) -> bool:
        return self.__gt__(other) or self.__eq__(other)

    def __len__(self) -> int:
        return self.km


distance = Distance(50)
# distance < Distance(60)  # True  # distance.km < 60 == True
# distance > Distance(120)  # False
# distance == Distance(100)  # False
# distance <= Distance(49)  # False
# distance >= Distance(50)
print(distance < Distance(60))