from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, value: Distance | int | float) -> Distance:
        result = Distance.check_value(value)
        return Distance(self.km + result)

    def __iadd__(self, value: Distance | int | float) -> Distance:
        result = Distance.check_value(value)
        self.km = self.km + result
        return self

    def __mul__(self, value: int | float) -> Distance:
        return Distance(self.km * value)

    def __truediv__(self, value: int | float) -> Distance:
        return Distance(round(self.km / value, 2))

    def __lt__(self, value: Distance | int | float) -> bool:
        result = Distance.check_value(value)
        return self.km < result

    def __gt__(self, value: Distance | int | float) -> bool:
        result = Distance.check_value(value)
        return self.km > result

    def __eq__(self, value: Distance | int | float) -> bool:
        result = Distance.check_value(value)
        return self.km == result

    def __le__(self, value: Distance | int | float) -> bool:
        result = Distance.check_value(value)
        return self.km <= result

    def __ge__(self, value: Distance | int | float) -> bool:
        result = Distance.check_value(value)
        return self.km >= result

    @staticmethod
    def check_value(value: Distance | int | float) -> int:
        return value.km if isinstance(value, Distance) else value
