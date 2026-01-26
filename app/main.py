class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def _value(self, other):
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __eq__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km == value

    def __lt__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km < value

    def __le__(self, other):
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km <= value

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



