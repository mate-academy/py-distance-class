from __future__ import annotations


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> int or float or Distance:
        if not isinstance(other, Distance):
            distance = Distance(self.km + other)
        else:
            distance = Distance(self.km + other.km)
        return distance

    def __iadd__(self, other: Distance) -> Distance:
        if not isinstance(other, Distance):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, num: int) -> Distance:
        distance = Distance(self.km * num)
        return distance

    def __truediv__(self, num: int) -> Distance:
        distance = Distance(round(self.km / num, 2))
        return distance

    def __lt__(self, num: int or float or Distance) -> bool:
        if isinstance(num, Distance):
            return self.km < num.km
        else:
            return self.km < num

    def __gt__(self, num: int) -> bool:
        return self.km > num

    def __eq__(self, num: int) -> bool:
        return self.km == num

    def __le__(self, num: int) -> bool:
        return self.km <= num

    def __ge__(self, num: int) -> bool:
        return self.km >= num

    def __len__(self) -> float or int:
        return self.km
