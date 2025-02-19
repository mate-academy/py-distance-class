from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, addends: Distance | int | float) -> Distance:
        if isinstance(addends, int | float):
            return Distance(self.km + addends)

        return Distance(self.km + addends.km)

    def __iadd__(self, addends: Distance | int | float) -> Distance:
        self.km = self + addends

        return self

    def __mul__(self, multiplier: int | float) -> Distance:
        return Distance(self.km * multiplier)

    def __truediv__(self, divisor: int | float) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other_el: Distance | int | float) -> bool:
        if isinstance(other_el, Distance):
            return self.km < other_el.km

        return self.km < other_el

    def __gt__(self, other_el: Distance | int | float) -> bool:
        if isinstance(other_el, Distance):
            return self.km > other_el.km

        return self.km > other_el

    def __eq__(self, other_el: Distance | int | float) -> bool:
        if isinstance(other_el, Distance):
            return self.km == other_el.km

        return self.km == other_el

    def __le__(self, other_el: Distance | int | float) -> bool:
        return not self > other_el

    def __ge__(self, other_el: Distance | int | float) -> bool:
        return not self < other_el
