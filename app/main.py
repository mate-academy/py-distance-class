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
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other):
        # щоб працювало 10 + Distance(...)
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other):
        # щоб працювало 5 * Distance(...)
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = round(self.km / other, 2)
            return Distance(result)
        return NotImplemented

    def _compare_value(self, other):
        if isinstance(other, Distance):
            return self.km, other.km
        elif isinstance(other, (int, float)):
            return self.km, other
        else:
            return NotImplemented, NotImplemented

    def __lt__(self, other):
        self_val, other_val = self._compare_value(other)
        if self_val is NotImplemented:
            return NotImplemented
        return self_val < other_val

    def __gt__(self, other):
        self_val, other_val = self._compare_value(other)
        if self_val is NotImplemented:
            return NotImplemented
        return self_val > other_val

    def __eq__(self, other):
        self_val, other_val = self._compare_value(other)
        if self_val is NotImplemented:
            return NotImplemented
        return self_val == other_val

    def __le__(self, other):
        self_val, other_val = self._compare_value(other)
        if self_val is NotImplemented:
            return NotImplemented
        return self_val <= other_val

    def __ge__(self, other):
        self_val, other_val = self._compare_value(other)
        if self_val is NotImplemented:
            return NotImplemented
        return self_val >= other_val
