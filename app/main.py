from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, second: Distance | int | float) -> Distance:
        if isinstance(second, (int, float)):
            return Distance(self.km + second)
        return Distance(self.km + second.km)

    def __iadd__(self, second: Distance | int | float) -> Distance:
        if isinstance(second, (int, float)):
            self.km += second
            return self
        self.km += second.km
        return self

    def __mul__(self, second: int | float) -> Distance:
        return Distance(self.km * second)

    def __truediv__(self, second: int | float) -> Distance:
        return Distance(round(self.km / second, 2))

    def __eq__(self, second: Distance | int | float) -> bool:
        if isinstance(second, (int, float)):
            return self.km == second
        return self.km == second.km

    def __lt__(self, second: Distance | int | float) -> bool:
        if isinstance(second, (int, float)):
            return self.km < second
        return self.km < second.km

    def __gt__(self, second: Distance | int | float) -> bool:
        if isinstance(second, (int, float)):
            return self.km > second
        return self.km > second.km

    def __le__(self, second: Distance | int | float) -> bool:
        if isinstance(second, (int, float)):
            return self.km <= second
        return self.km <= second.km

    def __ge__(self, second: Distance | int | float) -> bool:
        if isinstance(second, (int, float)):
            return self.km >= second
        return self.km >= second.km
