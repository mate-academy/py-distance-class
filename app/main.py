from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @property
    def real(self) -> int | float:
        return self.km

    @real.setter
    def real(self, value: int | float) -> None:
        self.km = value

    def __str__(self) -> str:
        return f"Distance: {self.real} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.real})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(km=self.km + other.real)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += other.real
        return self

    def __mul__(self, num: int | float) -> Distance:
        return Distance(km=self.km * num)

    def __truediv__(self, num: int | float) -> Distance:
        trim_res = self.km / num
        return Distance(km=round(trim_res, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.real < other.real

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.real > other.real

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.real == other.real

    def __le__(self, other: Distance | int | float) -> bool:
        return self.real <= other.real

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.real >= other.real

    def __len__(self) -> int:
        return self.km
