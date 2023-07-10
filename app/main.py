from typing import Type


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km
        self.real = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(
            self,
            other: Type["Distance"] | int | float
    ) -> Type["Distance"]:
        return Distance(self.real + other.real)

    def __iadd__(
            self,
            other: Type["Distance"] | int | float
    ) -> Type["Distance"]:
        self.real += other.real
        self.km += other.real
        return self

    def __mul__(self, other: int | float) -> Type["Distance"]:
        if isinstance(other, Distance):
            raise TypeError()
        return Distance(self.real * other.real)

    def __truediv__(self, other: int | float) -> Type["Distance"]:
        if isinstance(other, Distance):
            raise TypeError()
        return Distance(round(self.real / other.real, 2))

    def __lt__(self, other: Type["Distance"]) -> bool:
        if self.real < other.real:
            return True
        return False

    def __gt__(self, other: Type["Distance"]) -> bool:
        if self.real > other.real:
            return True
        return False

    def __eq__(self, other: Type["Distance"]) -> bool:
        if self.real == other.real:
            return True
        return False

    def __le__(self, other: Type["Distance"]) -> bool:
        if self.real <= other.real:
            return True
        return False

    def __ge__(self, other: Type["Distance"]) -> bool:
        if self.real >= other.real:
            return True
        return False
