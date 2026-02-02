class Distance:
    def __init__(self, km: float) -> float:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> float:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        if isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: float) -> float:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self

    def __mul__(self, other: float) -> float:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: float) -> float:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def _get_value(self, other: float) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __lt__(self, other: float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km < value

    def __gt__(self, other: float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km > value

    def __eq__(self, other: float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km == value

    def __le__(self, other: float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other: float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km >= value
