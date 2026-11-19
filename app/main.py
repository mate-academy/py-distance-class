class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    @staticmethod
    def _extract_km(other):
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)) and not isinstance(other, bool):
            return other
        return NotImplemented

    def __add__(self, other):
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other):
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, factor):
        if isinstance(factor, (int, float)) and not isinstance(factor, bool):
            return Distance(self.km * factor)
        return NotImplemented

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)) and not isinstance(divisor, bool):
            return Distance(round(self.km / divisor, 2))
        return NotImplemented

    def __lt__(self, other):
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __gt__(self, other):
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other):
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return False
        return self.km == other_km

    def __le__(self, other):
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other):
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km