class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, (Distance, int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, (Distance, int, float)) and other:
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance | float | int") -> bool:
        return self.km < other

    def __gt__(self, other: "Distance | float | int") -> bool:
        return self.km > other

    def __eq__(self, other: "Distance | float | int") -> bool:
        return self.km == other

    def __le__(self, other: "Distance | float | int") -> bool:
        return self.km <= other

    def __ge__(self, other: "Distance | float | int") -> bool:
        return self.km >= other
