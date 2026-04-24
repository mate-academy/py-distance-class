class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> Distance:
        if isinstance(other, (Distance, int, float)):
            other_km = other.km if isinstance(other, Distance) else other
        else:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other: "Distance | int | float") -> Distance:
        if isinstance(other, (Distance, int, float)):
            other_km = other.km if isinstance(other, Distance) else other
            self.km += other_km
        else:
            return NotImplemented
        return self

    def __mul__(self, other: "Distance | int | float") -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            return NotImplemented

    def __truediv__(self, other: "Distance | int | float") -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round((self.km / other), 2))
        else:
            return NotImplemented

    def __lt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            other_km = other.km if isinstance(other, Distance) else other
            return self.km < other_km
        else:
            return NotImplemented

    def __gt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            other_km = other.km if isinstance(other, Distance) else other
            return self.km > other_km
        else:
            return NotImplemented

    def __eq__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            other_km = other.km if isinstance(other, Distance) else other
            return self.km == other_km
        else:
            return NotImplemented

    def __le__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            other_km = other.km if isinstance(other, Distance) else other
            return self.km <= other_km
        else:
            return NotImplemented

    def __ge__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            other_km = other.km if isinstance(other, Distance) else other
            return self.km >= other_km
        else:
            return NotImplemented
