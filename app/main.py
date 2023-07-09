from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: Distance | int | float) -> Distance:
        return (
            Distance(self.km + distance.km)
            if isinstance(distance, Distance)
            else Distance(self.km + distance)
        )

    def __iadd__(self, distance: Distance | int | float) -> Distance:
        self.km += distance.km if isinstance(distance, Distance) else distance
        return self

    def __mul__(self, distance: Distance | int | float) -> Distance:
        return (
            Distance(self.km * distance.km)
            if isinstance(distance, Distance)
            else Distance(self.km * distance)
        )

    def __truediv__(self, distance: Distance | int | float) -> Distance:
        return (
            Distance(self.km / distance.km)
            if isinstance(distance, Distance)
            else Distance(self.km / distance)
        )

    def __lt__(self, distance: Distance | int | float) -> bool:
        return (
            self.km < distance.km
            if isinstance(distance, Distance)
            else self.km < distance
        )

    def __gt__(self, distance: Distance | int | float) -> bool:
        return (
            self.km > distance.km
            if isinstance(distance, Distance)
            else self.km > distance
        )

    def __eq__(self, distance: Distance | int | float) -> bool:
        return (
            self.km == distance.km
            if isinstance(distance, Distance)
            else self.km == distance
        )

    def __le__(self, distance: Distance | int | float) -> bool:
        return (
            self.km <= distance.km
            if isinstance(distance, Distance)
            else self.km <= distance
        )

    def __ge__(self, distance: Distance | int | float) -> bool:
        return (
            self.km >= distance.km
            if isinstance(distance, Distance)
            else self.km >= distance
        )
