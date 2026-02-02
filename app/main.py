class Distance:
    # Write your code here
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "int | float | 'Distance'") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: "int | float | 'Distance'") -> "Distance":
        self.km += other if isinstance(other, (int, float)) else other.km
        return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: float) -> bool:
        return self.km < other

    def __gt__(self, other: float) -> bool:
        return self.km > other

    def __eq__(self, other: float) -> bool:
        return self.km == other

    def __le__(self, other: float) -> bool:
        return self.km <= other

    def __ge__(self, other: float) -> bool:
        return self.km >= other
