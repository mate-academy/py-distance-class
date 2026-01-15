from __future__ import annotations
from types import NotImplementedType


class Distance:
    km: float

    def __init__(self, km: float | int) -> None:
        # przechowujemy jako float, bo po dzieleniu mogą pojawić się ułamki
        self.km = float(km)

    def __str__(self) -> str:
        km_out = int(self.km) if float(self.km).is_integer() else self.km
        return f"Distance: {km_out} kilometers."

    def __repr__(self) -> str:
        km_out = int(self.km) if float(self.km).is_integer() else self.km
        return f"Distance(km={km_out})"

    def __add__(
        self, other: "Distance" | float | int
    ) -> "Distance" | NotImplementedType:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + float(other))
        return NotImplemented

    def __iadd__(self, other: "Distance" | float | int) -> "Distance" | NotImplementedType:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += float(other)
        else:
            return NotImplemented  # pozwól Pythonowi użyć fallbacku do __add__
        return self

    def __mul__(self, other: float | int) -> "Distance" | NotImplementedType:
        if isinstance(other, (int, float)):
            return Distance(self.km * float(other))
        return NotImplemented

    def __truediv__(
        self, other: float | int
    ) -> "Distance" | NotImplementedType:
        if isinstance(other, (int, float)):
            wynik = round(self.km / float(other), 2)
            return Distance(wynik)
        return NotImplemented

    # porównania
    def __lt__(self, other: "Distance" | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < float(other)
        return False

    def __gt__(self, other: "Distance" | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > float(other)
        return False

    def __eq__(self, other: "Distance" | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == float(other)
        return False

    def __le__(self, other: "Distance" | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= float(other)
        return False

    def __ge__(self, other: "Distance" | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= float(other)
        return False
