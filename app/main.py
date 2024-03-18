from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km
        self.real = self.km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        return Distance(km=self.km + other.real)

    def __iadd__(self, other: Distance | int) -> Distance:
        self.km += other.real
        return self

    def __mul__(self, num: int) -> Distance:
        return Distance(km=self.km * num)

    def __truediv__(self, num: int) -> Distance:
        trim_res = self.km / num
        return Distance(km=round(trim_res, 2))

    def __lt__(self, other: Distance | int) -> bool:
        return self.real < other.real

    def __gt__(self, other: Distance | int) -> bool:
        return self.real > other.real

    def __eq__(self, other: Distance | int) -> bool:
        return self.real == other.real

    def __le__(self, other: Distance | int) -> bool:
        return self.real <= other.real

    def __ge__(self, other: Distance | int) -> bool:
        return self.real >= other.real

    def __len__(self) -> int:
        return self.km
