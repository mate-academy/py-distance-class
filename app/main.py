from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: Distance | int | float) -> Distance:
        return Distance(self.km + self.get_km(other_distance))

    def __iadd__(self, other_distance: Distance | int | float) -> Distance:
        self.km += +self.get_km(other_distance)
        return self

    def __mul__(self, other_distance: Distance | int | float) -> Distance:
        self.check_if_number(other_distance)
        return Distance(self.km * self.get_km(other_distance))

    def __truediv__(self, other_distance: Distance | int) -> Distance:
        self.check_if_number(other_distance)
        return Distance(round(self.km / self.get_km(other_distance), 2))

    def __eq__(self, other_distance: Distance | int | float) -> bool:
        return self.km == self.get_km(other_distance)

    def __lt__(self, other_distance: Distance | int | float) -> bool:
        return self.km < self.get_km(other_distance)

    def __gt__(self, other_distance: Distance | int | float) -> bool:
        return self.km > self.get_km(other_distance)

    def __le__(self, other_distance: Distance | int | float) -> bool:
        return self.km <= self.get_km(other_distance)

    def __ge__(self, other_distance: Distance | int | float) -> bool:
        return self.km >= self.get_km(other_distance)

    @staticmethod
    def check_if_number(item: Distance | float | int) -> None:
        if not isinstance(item, (int, float)):
            raise TypeError("Method accept only numbers")

    @staticmethod
    def get_km(item: Distance | int | float) -> int | float:
        return item if type(item) == int or type(item) == float else item.km
