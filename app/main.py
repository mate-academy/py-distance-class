class Distance:
    def __init__(self, km: float = 0.0) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other:  Distance | int | float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other:  Distance | int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, factor:  int | float) -> "Distance":
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        return NotImplemented

    def __truediv__(self, divisor: int | float) -> "Distance":
        # if divisor == 0:
        # #     return NotImplemented
        # if isinstance(divisor, Distance):
        #     return Distance(round((self.km / divisor.km), 2))
        if isinstance(divisor, (int, float)):
            return Distance(round((self.km / divisor), 2))
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < float(other)
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > float(other)
        return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == float(other)
        return False

    def __le__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= float(other)
        return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= float(other)
        return NotImplemented
