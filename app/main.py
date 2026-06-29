class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_value(self, other):
        return other.km if isinstance(other, Distance) else other

    def __add__(self, other):
        return Distance(self.km + self._get_value(other))

    def __iadd__(self, other):
        self.km += self._get_value(other)
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        return self.km < self._get_value(other)

    def __gt__(self, other):
        return self.km > self._get_value(other)

    def __eq__(self, other):
        return self.km == self._get_value(other)

    def __le__(self, other):
        return self.km <= self._get_value(other)

    def __ge__(self, other):
        return self.km >= self._get_value(other)
