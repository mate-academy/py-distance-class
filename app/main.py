class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, km2: Distance | int | float) -> Distance:
        if isinstance(km2, Distance):
            return Distance(self.km + km2.km)
        elif isinstance(km2, (int, float)):
            return Distance(self.km + km2)

    def __iadd__(self, km2: Distance | int | float) -> Distance:
        if isinstance(km2, Distance):
            self.km += km2.km
        elif isinstance(km2, (int, float)):
            self.km += km2
        return self

    def __mul__(self, factor2: int | float) -> Distance:
        return Distance(self.km * factor2)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, dist2: Distance | int | float) -> bool | NotImplemented:
        if isinstance(dist2, Distance):
            return self.km < dist2.km
        elif isinstance(dist2, (int, float)):
            return self.km < dist2
        return NotImplemented

    def __gt__(self, dist2: Distance | int | float) -> bool | NotImplemented:
        if isinstance(dist2, Distance):
            return self.km > dist2.km
        elif isinstance(dist2, (int, float)):
            return self.km > dist2
        return NotImplemented

    def __eq__(self, dist2: Distance | int | float) -> bool | NotImplemented:
        if isinstance(dist2, Distance):
            return self.km == dist2.km
        elif isinstance(dist2, (int, float)):
            return self.km == dist2
        return NotImplemented

    def __le__(self, dist2: Distance | int | float) -> bool | NotImplemented:
        if isinstance(dist2, Distance):
            return self.km <= dist2.km
        elif isinstance(dist2, (int, float)):
            return self.km <= dist2
        return NotImplemented

    def __ge__(self, dist2: Distance | int | float) -> bool | NotImplemented:
        if isinstance(dist2, Distance):
            return self.km >= dist2.km
        elif isinstance(dist2, (int, float)):
            return self.km >= dist2
        return NotImplemented
