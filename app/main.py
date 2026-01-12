class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def to_kilometers(distance: float) -> float:
        if isinstance(distance, Distance):
            return float(distance.km)
        if isinstance(distance, (int, float)):
            return float(distance)

    def __add__(self, other: object) -> "Distance":
        other_km = self.to_kilometers(other)
        return Distance(self.km + other_km)

    def __iadd__(self, other: object) -> "Distance":
        other_km = self.to_kilometers(other)
        self.km += other_km
        return self

    def __mul__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: object) -> bool:
        other_km = self.to_kilometers(other)
        return self.km < other_km

    def __gt__(self, other: "Distance") -> bool:
        other_km = self.to_kilometers(other)
        return self.km > other_km

    def __eq__(self, other: "Distance") -> bool:
        other_km = self.to_kilometers(other)
        return self.km == other_km

    def __le__(self, other: "Distance") -> bool:
        other_km = self.to_kilometers(other)
        return self.km <= other_km

    def __ge__(self, other: "Distance") -> bool:
        other_km = self.to_kilometers(other)
        return self.km >= other_km
