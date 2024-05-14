class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: ["Distance", float]) -> "Distance":
        if isinstance(other, Distance):
            distance3: float = self.km + other.km
            return Distance(distance3)
        elif isinstance(other, (int, float)):
            distance3: float = self.km + other
            return Distance(distance3)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: [int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            distance2: float = self.km * other
            return Distance(distance2)

    def __truediv__(self, other: [int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            distance2: float = round(self.km / other, 2)
            return Distance(distance2)

    def __lt__(self, other: ["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: ["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: ["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: ["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: ["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
