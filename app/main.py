from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, km2: Any) -> Any:
        if isinstance(km2, Distance):
            return Distance(self.km + km2.km)
        elif isinstance(km2, (int, float)):
            return Distance(self.km + km2)
        return None

    def __iadd__(self, km2: Any) -> Any:
        if isinstance(km2, Distance):
            self.km += km2.km
        elif isinstance(km2, (int, float)):
            self.km += km2
        return self

    def __mul__(self, factor2: Any) -> Any:
        return Distance(self.km * factor2)

    def __truediv__(self, other: Any) -> Any:
        return Distance(round(self.km / other, 2))

    def __lt__(self, distance2: Any) -> bool:
        if isinstance(distance2, Distance):
            return self.km < distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km < distance2

    def __gt__(self, distance2: Any) -> bool:
        if isinstance(distance2, Distance):
            return self.km > distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km > distance2

    def __eq__(self, distance2: Any) -> bool:
        if isinstance(distance2, Distance):
            return self.km == distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km == distance2

    def __le__(self, distance2: Any) -> bool:
        if isinstance(distance2, Distance):
            return self.km <= distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km <= distance2

    def __ge__(self, distance2: Any) -> bool:
        if isinstance(distance2, Distance):
            return self.km >= distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km >= distance2
