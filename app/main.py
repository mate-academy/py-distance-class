class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        km_display = int(self.km) if self.km.is_integer() else self.km
        return f"Distance: {km_display} kilometers."

    def __repr__(self) -> str:
        km_display = int(self.km) if self.km.is_integer() else self.km
        return f"Distance(km={km_display})"

    # Addition
    def __add__(self, other) -> "Distance":
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __radd__(self, other) -> "Distance":
        return Distance(self.km + other)

    def __iadd__(self, other) -> "Distance":
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    # Multiplikation
    def __mul__(self, other) -> "Distance":
        return Distance(self.km * other)

    def __rmul__(self, other) -> "Distance":
        return Distance(self.km * other)

    # Division
    def __truediv__(self, other) -> "Distance":
        return Distance(round(self.km / other, 2))

    # Vergleich
    def __lt__(self, other) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __le__(self, other) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __eq__(self, other) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km == value

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __ge__(self, other) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value
