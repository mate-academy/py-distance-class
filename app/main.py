class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: object) -> "Distance":
        return self.__add__(other)

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: object) -> "Distance":
        return self.__mul__(other)

    def __truediv__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def _compare_value(self, other: object) -> tuple:
        if isinstance(other, Distance):
            return self.km, other.km
        if isinstance(other, (int, float)):
            return self.km, other
        return NotImplemented, NotImplemented

    def __lt__(self, other: object) -> bool:
        a, b = self._compare_value(other)
        if a is NotImplemented:
            return NotImplemented
        return a < b

    def __gt__(self, other: object) -> bool:
        a, b = self._compare_value(other)
        if a is NotImplemented:
            return NotImplemented
        return a > b

    def __eq__(self, other: object) -> bool:
        a, b = self._compare_value(other)
        if a is NotImplemented:
            return NotImplemented
        return a == b

    def __le__(self, other: object) -> bool:
        a, b = self._compare_value(other)
        if a is NotImplemented:
            return NotImplemented
        return a <= b

    def __ge__(self, other: object) -> bool:
        a, b = self._compare_value(other)
        if a is NotImplemented:
            return NotImplemented
        return a >= b
