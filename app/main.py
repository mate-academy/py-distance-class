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
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError
        return self

    def __mul__(self, other: float) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> "Distance":
        return Distance(round(self.km / other, 2))

    def _get_other_km(self, other: object) -> float | None:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return None

    def __lt__(self, other: object) -> bool:
        other_km = self._get_other_km(other)
        if other_km is None:
            return NotImplemented
        return self.km < other_km

    def __gt__(self, other: object) -> bool:
        other_km = self._get_other_km(other)
        if other_km is None:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other: object) -> bool:
        other_km = self._get_other_km(other)
        if other_km is None:
            return False
        return self.km == other_km

    def __le__(self, other: object) -> bool:
        other_km = self._get_other_km(other)
        if other_km is None:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other: object) -> bool:
        other_km = self._get_other_km(other)
        if other_km is None:
            return NotImplemented
        return self.km >= other_km
