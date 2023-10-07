from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, *args) -> Distance:
        if isinstance(*args, Distance):
            return Distance(self.km + args[0].km)
        return Distance(self.km + args[0])

    def __iadd__(self, *args) -> Distance:
        if isinstance(*args, Distance):
            self.km += args[0].km
        else:
            self.km += args[0]
        return self

    def __mul__(self, *args) -> Distance:
        if isinstance(*args, (int, float)):
            return Distance(self.km * args[0])

    def __truediv__(self, *args) -> Distance:
        if isinstance(*args, (int, float)):
            return Distance(round(self.km / args[0], 2))

    def __lt__(self, *args) -> bool:
        if isinstance(*args, Distance):
            return self.km < args[0].km
        return self.km < args[0]

    def __gt__(self, *args) -> bool:
        if isinstance(*args, Distance):
            return self.km > args[0].km
        return self.km > args[0]

    def __eq__(self, *args) -> bool:
        if isinstance(*args, Distance):
            return self.km == args[0].km
        return self.km == args[0]

    def __le__(self, *args) -> bool:
        if isinstance(*args, Distance):
            return self.km <= args[0].km
        return self.km <= args[0]

    def __ge__(self, *args) -> bool:
        if isinstance(*args, Distance):
            return self.km >= args[0].km
        return self.km >= args[0]
