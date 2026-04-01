class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: Distance) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __mul__(self, other: Distance) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Distance) -> Distance:
        return Distance(round(self.km / other, 2))

    def _get_cmp_value(self, other: Distance) -> Distance:
        return other.km if isinstance(other, Distance) else other

    def __lt__(self, other: Distance) -> bool:
        return self.km < self._get_cmp_value(other)

    def __gt__(self, other: Distance) -> bool:
        return self.km > self._get_cmp_value(other)

    def __eq__(self, other: Distance) -> bool:
        return self.km == self._get_cmp_value(other)

    def __le__(self, other: Distance) -> bool:
        return self.km <= self._get_cmp_value(other)

    def __ge__(self, other: Distance) -> bool:
        return self.km >= self._get_cmp_value(other)
