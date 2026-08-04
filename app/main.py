from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, outro: Distance | int | float) -> Distance:
        if isinstance(outro, (int, float)):
            return Distance(self.km + outro)
        return Distance(self.km + outro.km)

    def __iadd__(self, outro: Distance | int | float) -> Distance:
        if isinstance(outro, (int, float)):
            self.km += outro
            return self
        self.km += outro.km
        return self

    def __mul__(self, outro: int | float) -> Distance:
        return Distance(self.km * outro)

    def __truediv__(self, outro: Distance | int | float) -> Distance:
        return Distance(round((self.km / outro), 2))

    def __lt__(self, outro: Distance | int | float) -> bool:
        return self.km < outro

    def __gt__(self, outro: Distance | int | float) -> bool:
        return self.km > outro

    def __eq__(self, outro: Distance | int | float) -> bool:
        return self.km == outro

    def __le__(self, outro: Distance | int | float) -> bool:
        return self.km <= outro

    def __ge__(self, outro: Distance | int | float) -> bool:
        return self.km >= outro
