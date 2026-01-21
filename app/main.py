class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def _value(self, other):
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other):
        if isinstance(other, Distance):
            return NotImplemented
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return NotImplemented
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km < value

    def __gt__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km > value

    def __ge__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km >= value

    def __le__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km <= value

    def __eq__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km == value
