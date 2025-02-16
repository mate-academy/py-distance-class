class Distance:
    def __init__(self, km: (float, int)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> "Distance":
        if isinstance(other, (int, float)):
            result_km = self.km + other
        elif isinstance(other, Distance):
            result_km = self.km + other.km
        else:
            return NotImplemented
        return Distance(result_km)

    def __iadd__(self, other) -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            return NotImplemented
        return self

    def __mul__(self, other) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        elif isinstance(other, Distance):
            raise TypeError("Multiplication between two Distance instances is not supported")
        return NotImplemented

    def __truediv__(self, other) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round((self.km / other), 2))
        elif isinstance(other, Distance):
            raise TypeError("Division between two Distance instances is not supported")
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented
