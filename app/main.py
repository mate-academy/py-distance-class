from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: Distance | int) -> Distance:
        if isinstance(distance, Distance):
            return Distance(self.km + distance.km)

        return Distance(self.km + distance)

    def __iadd__(self, distance: Distance | int) -> Distance:
        if isinstance(distance, Distance):
            self.km += distance.km

        if isinstance(distance, int):
            self.km += distance

        return self
