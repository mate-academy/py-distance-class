from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            return self.calculate_real_num(other, "+")
        elif isinstance(other, Distance):
            return self.calculate_class_instance(other, "+")
        raise TypeError

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            raise TypeError
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return self.calculate_real_num(other, "*")
        raise TypeError

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return self.calculate_real_num(other, "/")
        raise TypeError

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        raise TypeError

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        raise TypeError

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km
        raise TypeError

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        raise TypeError

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        raise TypeError

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def calculate_class_instance(
            self,
            other: Distance,
            operator: str
    ) -> Distance:
        if operator == "+":
            return Distance(
                km=self.km + other.km,
            )

    def calculate_real_num(
            self,
            other: int | float,
            operator: str
    ) -> Distance:
        if operator == "+":
            return Distance(
                km=self.km + other,
            )
        elif operator == "*":
            return Distance(
                km=self.km * other
            )
        elif operator == "/":
            return Distance(
                km=round(self.km / other, 2),
            )
