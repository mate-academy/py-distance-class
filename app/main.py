from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: any) -> Distance:
        if isinstance(distance, Distance):
            return Distance(self.km + distance.km)
        elif isinstance(distance, float):
            return Distance(self.km + distance)
        elif isinstance(distance, int):
            return Distance(self.km + distance)

    def __iadd__(self, distance: any) -> Distance:
        if isinstance(distance, Distance):
            self.km += distance.km
        elif isinstance(distance, (float, int)):
            self.km += distance
        return self

    def __mul__(self, factor: float) -> float:
        return Distance(self.km * factor)

    def __truediv__(self, divisor: float) -> float:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, distance: any) -> bool:
        if isinstance(distance, Distance):
            return self.km < distance.km
        elif isinstance(distance, (float, int)):
            return self.km < distance

    def __gt__(self, distance: any) -> bool:
        if isinstance(distance, Distance):
            return self.km > distance.km
        elif isinstance(distance, (float, int)):
            return self.km > distance
        
    def __eq__(self, distance: any) -> bool:
        if isinstance(distance, Distance):
            return self.km == distance.km
        elif isinstance(distance, (float, int)):
            return self.km == distance

    def __le__(self, distance: any) -> bool:
        return self < distance or self == distance

    def __ge__(self, distance: any) -> bool:
        return self > distance or self == distance
