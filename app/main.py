class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, factor: "float | int") -> "Distance":
        return Distance(self.km * factor)

    def __truediv__(self, divisor: "float | int") -> "Distance":
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: "Distance | float | int") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other: "Distance | float | int") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other: "Distance | float | int") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km == other_km

    def __le__(self, other: "Distance | float | int") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other: "Distance | float | int") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
