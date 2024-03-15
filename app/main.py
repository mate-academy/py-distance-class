from __future__ import division


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, value: any) -> any:
        if isinstance(value, Distance):
            return Distance(self.km + value.km)

        return Distance(self.km + value)

    def __iadd__(self, value: any) -> any:
        if isinstance(value, Distance):
            self.km = self.km + value.km
            return self

        self.km = self.km + value
        return self

    def __mul__(self, value: any) -> any:
        self.km = self.km * value
        return self

    def __truediv__(self, value: any) -> any:
        self.km = round(self.km / value, 2)
        return self

    def __lt__(self, value: any) -> any:
        if isinstance(value, Distance):
            return self.km < value.km

        return self.km < value

    def __gt__(self, value: any) -> any:
        if isinstance(value, Distance):
            return self.km > value.km

        return self.km > value

    def __eq__(self, value: any) -> any:
        if isinstance(value, Distance):
            return self.km == value.km

        return self.km == value

    def __le__(self, value: any) -> any:
        if isinstance(value, Distance):
            return self.km <= value.km

        return self.km <= value

    def __ge__(self, value: any) -> any:
        if isinstance(value, Distance):
            return self.km >= value.km

        return self.km >= value
