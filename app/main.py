class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> 'Distance':
        if isinstance(other, (Distance, int, float)):
            return Distance(self.km + (other.km if isinstance(other, Distance) else other))
        return NotImplemented

    def __iadd__(self, other) -> 'Distance':
        if isinstance(other, (Distance, int, float)):
            self.km += (other.km if isinstance(other, Distance) else other)
            return self
        return NotImplemented

    def __mul__(self, value: float) -> 'Distance':
        if isinstance(value, (int, float)):
            return Distance(self.km * value)
        return NotImplemented

    def __truediv__(self, value: float) -> 'Distance':
        if isinstance(value, (int, float)):
            return Distance(round(self.km / value, 2))
        return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km == (other.km if isinstance(other, Distance) else other)
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        return NotImplemented
