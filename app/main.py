class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, dist: float) -> "Distance":
        if not isinstance(dist, Distance):
            dist = Distance(dist)
        return Distance(self.km + dist.km)

    def __iadd__(self, dist: float) -> "Distance":
        if not isinstance(dist, Distance):
            dist = Distance(dist)
        self.km += dist.km
        return self

    def __mul__(self, mult: int) -> "Distance":
        return Distance(self.km * mult)

    def __truediv__(self, div: int) -> "Distance":
        return Distance(round(self.km / div, 2))

    def __lt__(self, dist: int) -> bool:
        return True if self.km < dist else False

    def __gt__(self, dist: int) -> bool:
        return True if self.km > dist else False

    def __eq__(self, dist: int) -> bool:
        return True if self.km == dist else False

    def __le__(self, dist: int) -> bool:
        return True if self.km <= dist else False

    def __ge__(self, dist: int) -> bool:
        return True if self.km >= dist else False
