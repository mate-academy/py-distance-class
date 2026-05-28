class Distance:
    def __init__(self, km: int) -> "Distance":
        self.km = km

    def __str__(self) -> "Distance":
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> "Distance":
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other

        return Distance(self.km + value)

    def __iadd__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        self.km += value
        return self

    def __mul__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Cannot multiply Distance by Distance")

        return Distance(self.km * other)

    def __truediv__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Cannot divide Distance by Distance")

        return Distance(round(self.km / other, 2))

    def _get_value(self, other: int) -> "Distance":
        return other.km if isinstance(other, Distance) else other

    def __eq__(self, other: int) -> "Distance":
        return self.km == self._get_value(other)

    def __lt__(self, other: int) -> "Distance":
        return self.km < self._get_value(other)

    def __gt__(self, other: int) -> "Distance":
        return self.km > self._get_value(other)

    def __le__(self, other: int) -> "Distance":
        return self.km <= self._get_value(other)

    def __ge__(self, other: int) -> "Distance":
        return self.km >= self._get_value(other)
