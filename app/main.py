class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self: "Distance") -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: "Distance") -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
            return self
        elif isinstance(other, Distance):
            self.km += other.km
            return self
        return NotImplemented

    def __mul__(self, other: "Distance") -> "Distance":

        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented  # 47 pass

    def __truediv__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented
        # 51 pass but round badly,2.86 is not 2.85

    # -----------------------------------------------------------------------------

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        return NotImplemented

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        return NotImplemented

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km
        return NotImplemented

    def __ne__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km != other
        elif isinstance(other, Distance):
            return self.km != other.km
        return NotImplemented

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        return NotImplemented

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        return NotImplemented
