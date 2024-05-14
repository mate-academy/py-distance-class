class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: [int, float]) -> "Distance":
        if isinstance(other, Distance):
            distance3 = self.km + other.km
            return Distance(distance3)
        elif isinstance(other, (int, float)) or isinstance(other, float):
            distance3 = self.km + other
            return Distance(distance3)

    def __iadd__(self, other: [int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: [int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            distance2 = self.km * other
            return Distance(distance2)

    def __truediv__(self, other: [int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            distance2 = round(self.km / other, 2)
            return Distance(distance2)

    def __lt__(self, other: ["Distance", float]) -> bool:
        return self.km < other

    def __gt__(self, other: ["Distance", float]) -> bool:
        return self.km > other

    def __eq__(self, other: ["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: ["Distance", float]) -> bool:
        return self.km <= other

    def __ge__(self, other: ["Distance", float]) -> bool:
        return self.km >= other
