class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | float") -> "Distance":
        other_km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + other_km)

    def __iadd__(self, other: "Distance | float") -> "Distance":
        other_km = other.km if isinstance(other, Distance) else other
        self.km += other_km
        return self

    def __mul__(self, number: float) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: float) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: "Distance | float") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other: "Distance | float") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other: "Distance | float") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km == other_km

    def __le__(self, other: "Distance | float") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other: "Distance | float") -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
