class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> 'Distance':
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: object) -> 'Distance':
        return self.__add__(other)

    def __iadd__(self, other: object) -> 'Distance':
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, factor: float) -> 'Distance':
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        return NotImplemented

    def __rmul__(self, factor: float) -> 'Distance':
        return self.__mul__(factor)

    def __truediv__(self, divisor: float) -> 'Distance':
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Distance(round(self.km / divisor, 2))
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented


# Example usage:
distance1 = Distance(20)
distance2 = Distance(30)
print(distance1 + distance2)  # Distance: 50 kilometers.
print(distance1 * 2)  # Distance: 40 kilometers.
print(distance1 / 7)  # Distance: 2.86 kilometers.
print(distance1 < 25)  # True
