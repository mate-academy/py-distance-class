class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> object:
        if isinstance(other, Distance):
            new_distance_km = self.km + other.km
            return Distance(new_distance_km)
        elif isinstance(other, (int, float)):
            new_distance_km = self.km + other
            return Distance(new_distance_km)
        else:
            return NotImplemented

    def __iadd__(self, other: object) -> object:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            return NotImplemented

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            new_distance_km = self.km * other
            return Distance(new_distance_km)
        else:
            return NotImplemented

    def __truediv__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            new_distance = self.km / other
            return Distance(round(new_distance, 2))
        else:
            return NotImplemented

    def __lt__(self, other: object) -> object:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            return NotImplemented

    def __gt__(self, other: object) -> object:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            return NotImplemented

    def __eq__(self, other: object) -> object:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return NotImplemented

    def __le__(self, other: object) -> object:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            return NotImplemented

    def __ge__(self, other: object) -> object:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            return NotImplemented
