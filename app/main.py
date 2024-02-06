class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float)) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: (int, float)) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self  # Return self only once

    def __mul__(self, multiplier: float) -> "Distance":
        return Distance(self.km * multiplier)

    def __truediv__(self, divisor: float) -> "Distance":
        result = self.km / divisor
        return Distance(round(result, 2))

    def __lt__(self, other: (int, float)) -> bool:
        return (
            self.km < other.km
            if isinstance(other, Distance)
            else self.km < other
        )

    def __gt__(self, other: (int, float)) -> bool:
        return (
            self.km > other.km
            if isinstance(other, Distance)
            else self.km > other
        )

    def __eq__(self, other: (int, float)) -> bool:
        return (
            self.km == other.km
            if isinstance(other, Distance)
            else self.km == other
        )

    def __le__(self, other: (int, float)) -> bool:
        return (
            self.km <= other.km
            if isinstance(other, Distance)
            else self.km <= other
        )

    def __ge__(self, other: (int, float)) -> bool:
        return (
            self.km >= other.km
            if isinstance(other, Distance)
            else self.km >= other
        )
