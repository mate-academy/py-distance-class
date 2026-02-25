from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def get_raw_value(distance: Distance | int | float) -> int | float:
        if isinstance(distance, Distance):
            return distance.km
        return distance

    def __add__(self, distance: Distance | int | float) -> Distance:
        value1 = Distance.get_raw_value(self)
        value2 = Distance.get_raw_value(distance)
        return Distance(value1 + value2)

    def __iadd__(self, distance: Distance | int | float) -> Distance:
        self.km += Distance.get_raw_value(distance)
        return self

    def __mul__(self, amount: int | float) -> Distance:
        return Distance(self.km * amount)

    def __truediv__(self, amount: int | float) -> Distance:
        return Distance(round(self.km / amount, 2))

    def __lt__(self, distance: Distance | int | float) -> bool:
        return (
            Distance.get_raw_value(self) < Distance.get_raw_value(distance)
        )

    def __gt__(self, distance: Distance | int | float) -> bool:
        return (
            Distance.get_raw_value(self) > Distance.get_raw_value(distance)
        )

    def __eq__(self, distance: Distance | int | float) -> bool:
        return (
            Distance.get_raw_value(self) == Distance.get_raw_value(distance)
        )

    def __le__(self, distance: Distance | int | float) -> bool:
        return (
            Distance.get_raw_value(self) <= Distance.get_raw_value(distance)
        )

    def __ge__(self, distance: Distance | int | float) -> bool:
        return (
            Distance.get_raw_value(self) >= Distance.get_raw_value(distance)
        )
