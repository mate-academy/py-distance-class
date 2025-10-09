class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return NotImplemented

    def __iadd__(self, other) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            return NotImplemented

    def __mul__(self, other) -> NotImplemented:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            return NotImplemented

    def __rmul__(self, other) -> NotImplemented:
        return self.__mul__(other)

    def __truediv__(self, other) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError()
            value = self.km / other
            value = round(value, 2)
            return Distance(value)

        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km <= other
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km >= other
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            return NotImplemented
