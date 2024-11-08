from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, arg: Distance | int) -> Distance:
        if isinstance(arg, Distance):
            return Distance(self.km + arg.km)
        else:
            return Distance(self.km + arg)

    def __iadd__(self, arg: Distance | int) -> Distance:
        if isinstance(arg, Distance):
            self.km += arg.km
            return self
        else:
            self.km += arg
            return self

    def __mul__(self, arg: int) -> Distance:
        return Distance(self.km * arg)

    def __truediv__(self, arg: int) -> Distance:
        return Distance(round(self.km / arg, 2))

    def __lt__(self, arg: Distance | int) -> bool:
        if isinstance(arg, Distance):
            return self.km < arg.km
        else:
            return self.km < arg

    def __gt__(self, arg: Distance | int) -> bool:
        if isinstance(arg, Distance):
            return self.km > arg.km
        else:
            return self.km > arg

    def __eq__(self, arg: Distance | int) -> bool:
        if isinstance(arg, Distance):
            return self.km == arg.km
        else:
            return self.km == arg

    def __le__(self, arg: Distance | int) -> bool:
        if isinstance(arg, Distance):
            return self.km <= arg.km
        else:
            return self.km <= arg

    def __ge__(self, arg: Distance | int) -> bool:
        if isinstance(arg, Distance):
            return self.km >= arg.km
        else:
            return self.km >= arg
